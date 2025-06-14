from textual.widgets import Static

class LicenseView(Static):
    def on_mount(self):
        self.update("🔐 Vue Licence")
