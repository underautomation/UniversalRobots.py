# Point d'entrée principal de l'application Textual
import sys
# Ajout du chemin du projet pour permettre les imports locaux
sys.path.insert(0, r"C:\Users\hfr10\Downloads\UniversalRobots-project")

# Importations Textual pour la structure de l'application
from textual.app import App, ComposeResult
from textual.widgets import Footer, Label, Static
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import ListView, ListItem

# Import des vues personnalisées
from views.connection_view import ConnectionView
from views.dashboard_view import DashboardView
from views.license_view import LicenseView
from views.primary_interface_view import PrimaryInterfaceView
from views.rtde_view import RtdeView
from views.running_program_view import RunningProgramView
from views.sftp_view import SftpView

# Import du SDK Universal Robots
from underautomation.universal_robots.ur import UR


class UniversalRobotsApp(App):
    CSS_PATH = "styles.css"  # Fichier de styles CSS externe
    TITLE = "UnderAutomation"  # Titre de l'application

    def __init__(self):
        super().__init__()
        # Connexion initiale au robot à l'adresse IP par défaut
        self.ur = UR("127.0.0.1")  # Modifier si besoin selon ton réseau

    def compose(self) -> ComposeResult:
        # Barre supérieure avec le lien vers le site de la lib
        yield Horizontal(
            Static("[link=https://underautomation.com/universalrobots]UnderAutomation[/link]", id="app-link"),
            id="header"
        )

        # Corps principal : sidebar gauche + conteneur de vue
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
                    ListItem(Label("Q. Quitter", id="quit")),
                    id="menu-list"
                ),
                id="sidebar"
            ),
            Container(id="main-view"),  # Conteneur pour afficher les vues dynamiques
            id="body-container"
        )

        # Footer standard Textual (barre d'infos en bas)
        yield Footer()

    def on_mount(self) -> None:
        # Une fois l'app montée, on récupère le conteneur principal
        self.main_view = self.query_one("#main-view", Container)
        self.main_view.styles.height = "100%"  # S'assure que la vue prend toute la hauteur

    def show_view(self, view) -> None:
        # Change dynamiquement le contenu du conteneur principal
        self.main_view.remove_children()  # Nettoie la vue actuelle
        self.main_view.mount(view)       # Monte la nouvelle vue

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        # Gestion de la navigation par sélection dans la liste
        label = event.item.query_one(Label)
        selected_id = label.id

        if event.list_view.id == "menu-list":
            match selected_id:
                case "conn":
                    self.show_view(ConnectionView())
                case "dash":
                    view = DashboardView()
                    view.set_ur(self.ur)  # Passage de l'instance UR
                    self.show_view(view)
                case "lic":
                    self.show_view(LicenseView(self.ur))
                case "prim":
                    self.show_view(PrimaryInterfaceView(self.ur))
                case "rtde":
                    self.show_view(RtdeView(self.ur))
                case "prog":
                    self.show_view(RunningProgramView(self.ur))
                case "sftp":
                    self.show_view(SftpView(self.ur))
                case "quit":
                    self.exit()  # Quitte proprement l'application


# Point de démarrage de l'application
if __name__ == "__main__":
    UniversalRobotsApp().run()
