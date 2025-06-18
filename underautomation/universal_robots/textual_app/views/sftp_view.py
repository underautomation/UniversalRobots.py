# views/sftp_view.py

from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Button, Input, DataTable, Label
from textual.app import ComposeResult

class SftpView(Vertical):
    def __init__(self, ur):
        super().__init__()
        self.ur = ur
        self.sftp = self.ur.sftp
        self.current_path = "/"

        # Widgets
        self.path_label = Label(self.current_path)
        self.table = DataTable(zebra_stripes=True)
        self.table.add_columns("Name", "Type")

        self.input_path = Input(placeholder="Upload local file path...")
        self.upload_btn = Button("Upload", id="btn_upload")
        self.prev_btn = Button("Back", id="btn_back")
        self.refresh_btn = Button("Refresh", id="btn_refresh")

    def compose(self) -> ComposeResult:
        yield Static("SFTP Explorer", classes="view-title")
        yield self.path_label
        yield self.table
        with Horizontal():
            yield self.input_path
            yield self.upload_btn
        with Horizontal():
            yield self.prev_btn
            yield self.refresh_btn

    async def on_mount(self):
        self.refresh_table()

    def is_sftp_connected(self) -> bool:
        if hasattr(self.sftp, 'connected'):
            return self.sftp.connected
        if callable(getattr(self.sftp, 'is_connected', None)):
            return self.sftp.is_connected()
        return False

    def refresh_table(self):
        self.table.clear()
        if not self.is_sftp_connected():
            self.path_label.update("SFTP not connected")
            return

        if not self.current_path.endswith("/"):
            self.current_path += "/"

        self.path_label.update(f"Path: {self.current_path}")
        try:
            files = self.sftp.list_directory(self.current_path)
            for file in files:
                if file.name in (".", ".."):
                    continue
                ftype = "DIR" if file.is_directory else "FILE"
                self.table.add_row(file.name, ftype)
        except Exception as e:
            self.path_label.update(f"Error: {e}")

    async def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "btn_upload":
            local_path = self.input_path.value.strip()
            if local_path:
                self.upload_file(local_path)

        elif event.button.id == "btn_back":
            import os
            p = self.current_path.rstrip("/")
            parent = os.path.dirname(p)
            if not parent:
                parent = "/"
            self.current_path = parent
            self.refresh_table()

        elif event.button.id == "btn_refresh":
            self.refresh_table()

    def upload_file(self, local_path):
        import os, time

        if not self.is_sftp_connected():
            self.path_label.update("SFTP not connected")
            return

        if not os.path.isfile(local_path):
            self.path_label.update("Local file not found")
            return

        try:
            with open(local_path, "rb") as f:
                remote_path = self.current_path + os.path.basename(local_path)
                self.sftp.upload_file(f, remote_path)

            time.sleep(0.5)
            self.refresh_table()
            self.path_label.update(f"Uploaded: {os.path.basename(local_path)}")
        except Exception as e:
            self.path_label.update(f"Upload failed: {e}")

    async def on_data_table_row_highlighted(self, message: DataTable.RowHighlighted):
        selected = self.table.get_row_at(message.row_key)
        name, ftype = selected
        if ftype == "DIR":
            # Change de dossier puis rafraîchit la table
            self.current_path = self.current_path.rstrip("/") + "/" + name
            self.refresh_table()
