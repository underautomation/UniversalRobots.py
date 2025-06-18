from textual.containers import Vertical
from textual.widgets import Static, Input, Button
from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.license.license_state import LicenseState

# Petit widget maison pour afficher des logs texte dans l'UI (remplace un TextLog ou un terminal)
class SimpleLog(Static):
    def __init__(self):
        super().__init__()
        self.lines = []  # Stocke les lignes de log

    def write(self, message: str):
        self.lines.append(message)  # Ajoute une ligne
        self.lines = self.lines[-100:]  # Garde les 100 dernières lignes max
        self.update("\n".join(self.lines))  # Met à jour le rendu du widget avec tout le contenu
        

# Vue principale de gestion de la licence robot
class LicenseView(Vertical):
    def __init__(self, ur: UR):
        super().__init__()
        self.license_valid = False  # Permet de savoir si la licence est OK ou pas

        # Champs d'entrée pour la licence
        self.licensee_input = Input(placeholder="Licensee")
        self.key_input = Input(placeholder="License Key")
        self.license_info_log = SimpleLog()  # Zone d'affichage des infos de licence

        # Bouton de validation
        self.set_button = Button("Set License", id="set_license")

        self.ur = ur  # Référence à l'instance UR, injectée à l'initialisation

    # Construction du layout avec les widgets
    def compose(self):
        yield Static("License", classes="view-title")  # Titre visuel
        yield self.licensee_input
        yield self.key_input
        yield self.set_button
        yield Static("License Information")  # Titre de la zone d'infos
        yield self.license_info_log  # Log affichant l'état ou erreurs de licence

    # Appelé au montage de la vue (dès qu'elle est affichée)
    async def on_mount(self):
        try:
            from config import Config  # On récupère les données de config si elles existent

            # Pré-remplit les champs à partir du fichier de config
            self.licensee_input.value = Config.current.licensee
            self.key_input.value = Config.current.key

            # Essaie de valider la licence dès le lancement
            self.ur.register_license(Config.current.licensee, Config.current.key)
            self.update_license_controls()  # Met à jour l’affichage selon état réel
        except Exception as e:
            # Si ça plante (pas de config, mauvais format, etc.), on log l’erreur
            self.license_info_log.write(f"[red]Erreur lors du chargement de la licence: {e}")

    # Gère le clic sur le bouton "Set License"
    async def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "set_license":
            licensee = self.licensee_input.value
            key = self.key_input.value

            # Enregistre la licence dans le robot
            self.ur.register_license(licensee, key)
            self.update_license_controls()  # Rafraîchit les infos visuelles

            try:
                from config import Config  # Recharge la config (supposée modifiable)
                Config.current.licensee = licensee
                Config.current.key = key
                Config.save()  # Sauvegarde les nouvelles valeurs
            except Exception as e:
                self.license_info_log.write(f"[red]Erreur lors de la sauvegarde de la config: {e}")

    # Met à jour les éléments d'affichage selon la licence
    def update_license_controls(self):
        info = self.ur.license_info()  # Récupère toutes les infos de licence via l'API du SDK

        self.license_info_log.write("")  # On vide le log avant d'afficher proprement

        # Affiche toutes les infos retournées sous forme de string (obj `info` doit avoir une méthode __str__)
        self.license_info_log.write(f"[bold cyan]License Info:\n{info}")

        # États invalides de licence à surveiller (expired ou invalide)
        invalid_states = {
            getattr(LicenseState, 'Invalid', None),
            getattr(LicenseState, 'Expired', None)
        }
        invalid_states.discard(None)  # Supprime les None au cas où les attributs n’existent pas

        # Vérifie que l’état de la licence ne fait pas partie des états invalides
        if invalid_states:
            self.license_valid = getattr(info, 'state', None) not in invalid_states
        else:
            self.license_valid = True  # Si aucun état invalide trouvé, on suppose valide
