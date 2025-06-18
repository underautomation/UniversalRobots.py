from textual.containers import Vertical
from textual.widgets import Static, Input, Button
from textual.message import Message
from textual import events

from underautomation.universal_robots.ur import UR


class PrimaryInterfaceView(Vertical):
    def __init__(self, ur: UR):
        super().__init__()
        self.ur = ur  # On garde une référence à l'objet UR pour communiquer avec le robot
        self.script_input = Input(placeholder="Entrez un script UR ici…")  # Zone pour saisir un script à envoyer
        self.send_button = Button("Envoyer", id="send_script")  # Bouton pour envoyer le script saisi
        self.log_output = Static("En attente…")  # Zone texte pour afficher les messages de retour / statut

    def compose(self):
        # Construction de l'interface : un titre, la zone de script, le bouton, puis la zone de log
        yield Static("Interface primaire", classes="view-title")
        yield self.script_input
        yield self.send_button
        yield self.log_output

    async def on_mount(self):
        # Au montage du widget, on préremplit le script avec une valeur sauvegardée (si dispo)
        from config import Config
        self.script_input.value = Config.current.ur_script or ""

        # Si l'interface primaire UR est dispo, on essaie d'indiquer que c'est connecté
        # Le binding des événements est commenté car incompatible pour l'instant
        if self.ur and self.ur.primary_interface:
            try:
                # Ces lignes sont désactivées car l'objet n'expose pas les événements correctement pour l'instant
                # self.ur.primary_interface.popup_message_received += self._popup_message_received
                # self.ur.primary_interface.runtime_exception_message_received += self._runtime_exception_received
                self.log_output.update("[bold green]Interface primaire connectée (événements non liés).")
            except Exception as e:
                # En cas de problème avec les événements, on affiche l'erreur
                self.log_output.update(f"[bold red]Erreur lors de la connexion aux événements: {e}")
        else:
            # Si pas d'interface primaire, on informe l'utilisateur que ce n'est pas connecté
            self.log_output.update("[bold yellow]Interface primaire non connectée.")

    async def on_button_pressed(self, event: Button.Pressed):
        # Quand on appuie sur un bouton, on regarde lequel
        if event.button.id == "send_script":
            # Récupère le script entré, on enlève les espaces inutiles
            script = self.script_input.value.strip()
            if script:
                try:
                    # On envoie le script à l'interface primaire du robot
                    self.ur.primary_interface.send(script)
                    self.log_output.update("[bold green]Script envoyé.")
                except Exception as e:
                    # En cas d'erreur d'envoi, on affiche l'erreur
                    self.log_output.update(f"[bold red]Erreur d’envoi: {e}")
            else:
                # Si aucun script n'est saisi, on informe l'utilisateur
                self.log_output.update("[bold yellow]Aucun script à envoyer.")

    # Méthodes prévues pour gérer les événements (commentées pour l'instant)
    def _popup_message_received(self, sender, message):
        # Si un message popup est reçu, on l'affiche dans la zone de log en bleu
        self.log_output.update(f"[bold blue]Popup reçu: {message}")

    def _runtime_exception_received(self, sender, message):
        # Si une exception runtime est reçue, on l'affiche en rouge
        self.log_output.update(f"[bold red]Exception runtime: {message}")
