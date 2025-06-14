from textual.widgets import Static

class SftpView(Static):
    def on_mount(self):
        self.update("📁 Vue SFTP")
