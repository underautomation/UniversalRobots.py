from textual.widgets import Button, Static
from textual.containers import Vertical
from textual.widget import Widget

# Barre latérale avec les boutons de navigation principaux de l'application
class Sidebar(Widget):
    def compose(self):
        # Titre du menu + pile verticale de boutons
        yield Static("Menu Principal", id="menu-title")
        yield Vertical(
            Button("Connection", id="btn-connection"),         # Accès à la vue Connexion
            Button("Primary Interface", id="btn-primary"),     # Interface primaire
            Button("Dashboard", id="btn-dashboard"),           # Interface Dashboard
            Button("RTDE", id="btn-rtde"),                     # Interface RTDE
            Button("SFTP", id="btn-sftp"),                     # Explorateur SFTP
            Button("Running Program", id="btn-running"),       # Gestion programme en cours
            Button("License", id="btn-license"),               # Gestion de licence
        )
