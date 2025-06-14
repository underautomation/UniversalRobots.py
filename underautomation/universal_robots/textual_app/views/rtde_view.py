from textual.widgets import Static

class RtdeView(Static):
    def on_mount(self):
        self.update("📡 Vue RTDE")
