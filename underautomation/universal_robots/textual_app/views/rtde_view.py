from textual.containers import Vertical
from textual.widgets import Static, Button
from textual import events
from underautomation.universal_robots.ur import UR

class RtdeView(Vertical):
    def __init__(self, ur: UR):
        super().__init__()
        self.ur = ur  # Stocke l'instance UR pour interagir avec le robot

        self._log = Static()  # Zone texte privée pour afficher les logs et messages
        self.send_button = Button("Envoyer données RTDE", id="send_rtde_data")  # Bouton d'envoi des données RTDE

        # Vérifie si l'objet rtde a un attribut input_values (pour savoir si on peut envoyer des données)
        self.has_input_values = hasattr(self.ur.rtde, "input_values")

    def compose(self):
        # Construction de l'interface : un titre, le bouton d'envoi, puis la zone de log
        yield Static("Vue RTDE", classes="view-title")
        yield self.send_button

        # Mise à jour de la zone log selon la disponibilité des input_values RTDE
        if self.has_input_values:
            self._log.update("[bold green]RTDE input_values disponibles.")
        else:
            self._log.update("[bold red]Aucun input_values RTDE disponible.")

        yield self._log

    async def on_button_pressed(self, event: Button.Pressed):
        # Quand on clique sur un bouton, on regarde lequel
        if event.button.id == "send_rtde_data":
            # Si pas d'input_values, on bloque l'envoi et affiche un message d'erreur
            if not self.has_input_values:
                self._log.update("[bold red]Impossible d'envoyer: input_values indisponible.")
                return
            try:
                # On récupère les données input_values depuis l'objet rtde
                input_values = getattr(self.ur.rtde, "input_values", None)
                # On affiche les données dans la zone log pour confirmation (en cyan)
                self._log.update(f"[bold cyan]Données RTDE envoyées:\n{input_values}")
                # TODO: Ici il faudra ajouter la vraie logique pour envoyer ces données au robot
            except Exception as e:
                # Si une erreur survient lors de la récupération ou l'envoi, on l'affiche en rouge
                self._log.update(f"[bold red]Erreur lors de l'envoi RTDE: {e}")
