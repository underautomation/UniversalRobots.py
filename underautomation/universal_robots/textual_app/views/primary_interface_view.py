from textual.widgets import Static

class PrimaryInterfaceView(Static):
    def on_mount(self):
        self.update("🖥️ Vue Interface Primaire")
