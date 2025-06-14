from textual.widgets import Button, Static
from textual.containers import Vertical
from textual.widget import Widget

class Sidebar(Widget):
    def compose(self):
        yield Static("Menu Principal", id="menu-title")
        yield Vertical(
            Button("Connection", id="btn-connection"),
            Button("Primary Interface", id="btn-primary"),
            Button("Dashboard", id="btn-dashboard"),
            Button("RTDE", id="btn-rtde"),
            Button("SFTP", id="btn-sftp"),
            Button("Running Program", id="btn-running"),
            Button("Variables", id="btn-variables"),
            Button("License", id="btn-license"),
        )
