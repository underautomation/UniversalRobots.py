from textual.widgets import Static

class RunningProgramView(Static):
    def on_mount(self):
        self.update("🏃 Vue Programme en cours")
