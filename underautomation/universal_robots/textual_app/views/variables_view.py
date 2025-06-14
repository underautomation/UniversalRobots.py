from textual.widgets import Static

class VariablesView(Static):
    def on_mount(self):
        self.update("🔧 Vue Variables")
