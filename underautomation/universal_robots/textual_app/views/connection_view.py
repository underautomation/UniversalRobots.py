from textual.widgets import Button, Input, Label, Checkbox, Select
from textual.containers import Vertical, Horizontal, Container

# Import de l’API de contrôle du robot. Peut varier selon la lib réelle utilisée.
from underautomation.universal_robots import UR, ConnectParameters

class ConnectionView(Container):
    def compose(self):
        # Composition de l'interface utilisateur avec une disposition verticale
        yield Vertical(
            Label("Connexion au robot", id="title"),  # Titre principal

            Input(placeholder="Adresse IP", id="ip"),  # Champ pour l’adresse IP

            # Checkboxes pour activer différents services/interfaces du robot
            Checkbox("Primary Interface", id="primary_interface"),
            Checkbox("Dashboard", id="dashboard"),
            Checkbox("Interpreter Mode", id="interpreter"),
            Checkbox("XML-RPC", id="xmlrpc"),
            Input(placeholder="XML-RPC Port", id="xmlrpc_port"),  # Port XML-RPC (optionnel)

            # Section SSH/SFTP
            Checkbox("SSH", id="ssh"),
            Checkbox("SFTP", id="sftp"),
            Input(placeholder="Username SSH", id="ssh_user"),  # Identifiant SSH
            Input(password=True, placeholder="Password", id="ssh_password"),  # Mot de passe SSH

            # Communication via sockets
            Checkbox("Socket Communication", id="socket"),
            Input(placeholder="Socket Port", id="socket_port"),  # Port socket

            # RTDE (Real-Time Data Exchange)
            Checkbox("RTDE", id="rtde"),
            Label("Fréquence RTDE", id="freq_label"),
            Select(  # Sélection de la fréquence d’échantillonnage RTDE
                options=[
                    ("0 Hz", "0"),
                    ("50 Hz", "50"),
                    ("100 Hz", "100"),
                    ("250 Hz", "250"),
                    ("500 Hz", "500")
                ],
                id="rtde_freq"
            ),
            Select(  # Choix de la version du protocole RTDE
                options=[("RTDE v1", "v1"), ("RTDE v2", "v2")],
                id="rtde_version"
            ),

            # Boutons pour connexion/déconnexion
            Horizontal(
                Button("Connecter", id="connect_btn"),
                Button("Déconnecter", id="disconnect_btn"),
            ),

            Label("État: Déconnecté", id="status"),  # Label de statut de connexion

            id="connection_view"  # ID global de la vue
        )

    def on_mount(self):
        # Initialisation du statut à la création de la vue
        self.query_one("#status").update("État: Déconnecté")
        self.ur = None  # L’objet UR n’est pas encore instancié

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Détection de quel bouton a été cliqué et déclenchement des actions
        if event.button.id == "connect_btn":
            self.connect_robot()
        elif event.button.id == "disconnect_btn":
            self.disconnect_robot()

    def connect_robot(self):
        # Récupération de l’adresse IP entrée
        ip = self.query_one("#ip", Input).value
        if not ip:
            self.query_one("#status").update("Erreur : IP non renseignée")
            return

        try:
            self.ur = UR(ip)  # Instanciation de l’objet robot avec l’IP

            # Création de l’objet contenant tous les paramètres de connexion
            params = ConnectParameters()
            params.ip = ip

            # Configuration des services activés selon les checkbox cochées
            params.primary_interface.enable = self.query_one("#primary_interface", Checkbox).value
            params.dashboard.enable = self.query_one("#dashboard", Checkbox).value
            params.interpreter_mode.enable = self.query_one("#interpreter", Checkbox).value
            params.xmlrpc.enable = self.query_one("#xmlrpc", Checkbox).value

            # Port XML-RPC, conversion en entier uniquement si valide
            xmlrpc_port = self.query_one("#xmlrpc_port", Input).value
            params.xmlrpc.port = int(xmlrpc_port) if xmlrpc_port.isdigit() else 0

            # SSH et SFTP : valeurs + credentials
            params.ssh.enable_ssh = self.query_one("#ssh", Checkbox).value
            params.ssh.enable_sftp = self.query_one("#sftp", Checkbox).value
            params.ssh.username = self.query_one("#ssh_user", Input).value
            params.ssh.password = self.query_one("#ssh_password", Input).value

            # Communication par socket : état et port
            params.socket_communication.enable = self.query_one("#socket", Checkbox).value
            socket_port = self.query_one("#socket_port", Input).value
            params.socket_communication.port = int(socket_port) if socket_port.isdigit() else 0

            # RTDE : activation, fréquence et version
            params.rtde.enable = self.query_one("#rtde", Checkbox).value
            rtde_freq = self.query_one("#rtde_freq", Select).value
            params.rtde.frequency = int(rtde_freq) if rtde_freq.isdigit() else 0
            params.rtde.version = "V1" if self.query_one("#rtde_version", Select).value == "v1" else "V2"

            # Tentative de connexion au robot avec les paramètres
            self.ur.connect(params)
            self.query_one("#status").update("État: Connecté")

        except Exception as e:
            # Gestion des erreurs : affichage de l’exception et remise à None
            self.query_one("#status").update(f"Erreur de connexion : {e}")
            self.ur = None

    def disconnect_robot(self):
        # Si une instance UR existe, on tente la déconnexion
        if self.ur:
            try:
                self.ur.disconnect()
                self.query_one("#status").update("État: Déconnecté")
                self.ur = None
            except Exception as e:
                self.query_one("#status").update(f"Erreur déconnexion : {e}")
        else:
            # Si aucune connexion active, on informe l'utilisateur
            self.query_one("#status").update("Aucune connexion active")
