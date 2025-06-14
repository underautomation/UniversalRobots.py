from textual.app import App, ComposeResult
from textual.widgets import Footer, Label
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import ListView, ListItem

# Imports relatifs pour les vues
from views.connection_view import ConnectionView
from views.dashboard_view import DashboardView
from views.license_view import LicenseView
from views.primary_interface_view import PrimaryInterfaceView
from views.rtde_view import RtdeView
from views.running_program_view import RunningProgramView
from views.sftp_view import SftpView
from views.variables_view import VariablesView


class UniversalRobotsApp(App):
    CSS_PATH = "styles.css"
    TITLE = "Universal Robots Textual UI"

    def compose(self) -> ComposeResult:
        # Barre de titre centrée
        yield Container(
            Label("Universal Robots Textual UI", id="app-title"),
            id="header"
        )

        # Layout principal
        yield Horizontal(
            Vertical(
                Label("Menu", id="menu-title"),
                ListView(
                    ListItem(Label("1. Connexion", id="conn")),
                    ListItem(Label("2. Dashboard", id="dash")),
                    ListItem(Label("3. License", id="lic")),
                    ListItem(Label("4. Interface primaire", id="prim")),
                    ListItem(Label("5. RTDE", id="rtde")),
                    ListItem(Label("6. Programme en cours", id="prog")),
                    ListItem(Label("7. SFTP", id="sftp")),
                    ListItem(Label("8. Variables", id="vars")),
                    ListItem(Label("Q. Quitter", id="quit")),
                    id="menu-list"
                ),
                id="sidebar"
            ),
            Container(id="main-view"),
            id="body-container"
        )

        yield Footer()

    def on_mount(self) -> None:
        self.main_view = self.query_one("#main-view", Container)
        self.main_view.styles.height = "100%"

    def show_view(self, view) -> None:
        self.main_view.remove_children()
        self.main_view.mount(view)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        label = event.item.query_one(Label)
        selected_id = label.id

        if event.list_view.id == "menu-list":
            if selected_id == "conn":
                self.show_view(ConnectionView())
            elif selected_id == "dash":
                self.show_view(DashboardView())
            elif selected_id == "lic":
                self.show_view(LicenseView())
            elif selected_id == "prim":
                self.show_view(PrimaryInterfaceView())
            elif selected_id == "rtde":
                self.show_view(RtdeView())
            elif selected_id == "prog":
                self.show_view(RunningProgramView())
            elif selected_id == "sftp":
                self.show_view(SftpView())
            elif selected_id == "vars":
                self.show_view(VariablesView())
            elif selected_id == "quit":
                self.exit()


if __name__ == "__main__":
    UniversalRobotsApp().run()
