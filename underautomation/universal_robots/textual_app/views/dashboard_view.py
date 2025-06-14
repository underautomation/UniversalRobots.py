from textual.widgets import Static

class DashboardView(Static):
    def on_mount(self):
        self.update("📊 Vue Dashboard")
