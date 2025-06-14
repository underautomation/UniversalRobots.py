from textual.widgets import Static

class HeaderBar(Static):
    def compose(self):
        yield Static("Universal Robots Interface", classes="header-title")
