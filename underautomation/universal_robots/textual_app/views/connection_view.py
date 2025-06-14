from textual.widgets import Static

class ConnectionView(Static):
    def on_mount(self):
        self.update("🔌 Vue Connexion")
