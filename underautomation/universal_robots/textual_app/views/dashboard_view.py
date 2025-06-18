from textual.widgets import Static, Button, Input, Select
from textual.containers import VerticalScroll, Horizontal, Vertical
from textual.widget import Widget

from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.dashboard.operational_modes import OperationalModes
from underautomation.universal_robots.dashboard.user_roles import UserRoles

# Remplace un TextLog : simple logger visuel dans l’UI
class SimpleLog(Static):
    def __init__(self):
        super().__init__()
        self.lines = []  # Stocke les lignes de log

    def write(self, message: str):
        self.lines.append(message)
        self.lines = self.lines[-100:]  # Limite à 100 lignes max
        self.update("\n".join(self.lines))  # Affiche dans le widget

# Vue principale pour les commandes Dashboard
class DashboardView(Vertical):
    def __init__(self):
        super().__init__()
        self.ur: UR | None = None  # Instance du robot (injectée dynamiquement)
        self.console = SimpleLog()  # Console pour les logs

        # Champs texte pour différentes commandes
        self.program_input = Input(placeholder="Program path")
        self.popup_input = Input(placeholder="Popup message")
        self.log_input = Input(placeholder="Log message")
        self.installation_input = Input(placeholder="Installation path")
        self.custom_command_input = Input(placeholder="Custom dashboard command")
        self.variable_input = Input(placeholder="Variable name")

        # Liste déroulante des rôles utilisateur (dynamique)
        user_roles = [attr for attr in dir(UserRoles) if not attr.startswith('_')]
        self.role_select = Select([(name, name) for name in user_roles])

        # Liste déroulante des modes opérationnels (dynamique)
        operational_modes = [attr for attr in dir(OperationalModes) if not attr.startswith('_')]
        self.mode_select = Select([(name, name) for name in operational_modes])

    # Génère tous les widgets dans l’interface (UI)
    def compose(self):
        yield Static("Dashboard Remote Commands", classes="view-title")
        yield VerticalScroll(
            Button("Get Robot Mode", id="get_robot_mode"),
            Button("Power On", id="power_on"),
            Button("Power Off", id="power_off"),
            Button("Release Brake", id="release_brake"),
            Button("Unlock Protective Stop", id="unlock_stop"),
            Button("Shutdown", id="shutdown"),

            self.program_input,
            Button("Load Program", id="load_program"),
            Button("Get Loaded Program", id="get_loaded_program"),
            Button("Play", id="play"),
            Button("Pause", id="pause"),
            Button("Stop", id="stop"),
            Button("Is Program Running", id="is_running"),
            Button("Get Program State", id="get_prog_state"),
            Button("Is Program Saved", id="is_saved"),

            self.popup_input,
            Button("Show Popup", id="show_popup"),
            Button("Close Popup", id="close_popup"),

            self.log_input,
            Button("Add to Log", id="add_to_log"),
            Button("Get Polyscope Version", id="get_version"),

            self.installation_input,
            Button("Load Installation", id="load_installation"),

            Button("Get Serial Number", id="get_serial"),
            Button("Get Robot Model", id="get_model"),

            Button("Get Operational Mode", id="get_mode"),
            Button("Clear Operational Mode", id="clear_mode"),
            self.mode_select,
            Button("Set Operational Mode", id="set_mode"),

            self.role_select,
            Button("Set User Role", id="set_role"),

            Button("Is In Remote Control", id="in_remote"),
            Button("Get Safety Status", id="safety_status"),
            Button("Close Safety Popup", id="close_safety"),
            Button("Restart Safety", id="restart_safety"),

            self.custom_command_input,
            Button("Send Custom Command", id="custom_cmd"),

            self.variable_input,
            Button("Get Variable Value", id="get_var"),

            self.console  # Zone de log
        )

    # Permet d’injecter une instance de robot dans la vue
    def set_ur(self, ur: UR):
        self.ur = ur
        self.console.write("[cyan]UR object injected into dashboard view.")

    # Gestionnaire d’événement sur clic de bouton
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if not self.ur:
            self.console.write("[red]UR instance not set.")
            return

        cmd = event.button.id  # Récupère l’ID du bouton
        d = self.ur.dashboard  # Raccourci vers l’API dashboard

        try:
            # Utilise match-case pour exécuter la commande correspondante
            match cmd:
                case "get_robot_mode": self.log(d.get_robot_mode(), cmd)
                case "power_on": self.log(d.power_on(), cmd)
                case "power_off": self.log(d.power_off(), cmd)
                case "release_brake": self.log(d.release_brake(), cmd)
                case "unlock_stop": self.log(d.unlock_protective_stop(), cmd)
                case "shutdown": self.log(d.shutdown(), cmd)

                case "load_program":
                    path = self.program_input.value
                    self.log(d.load_program(path), cmd)
                case "get_loaded_program": self.log(d.get_loaded_program(), cmd)
                case "play": self.log(d.play(), cmd)
                case "pause": self.log(d.pause(), cmd)
                case "stop": self.log(d.stop(), cmd)
                case "is_running": self.log(d.is_program_running(), cmd)
                case "get_prog_state": self.log(d.get_program_state(), cmd)
                case "is_saved": self.log(d.is_program_saved(), cmd)

                case "show_popup":
                    msg = self.popup_input.value
                    self.log(d.show_popup(msg), cmd)
                case "close_popup": self.log(d.close_popup(), cmd)

                case "add_to_log":
                    msg = self.log_input.value
                    self.log(d.add_to_log(msg), cmd)

                case "get_version": self.log(d.get_polyscope_version(), cmd)

                case "load_installation":
                    path = self.installation_input.value
                    self.log(d.load_installation(path), cmd)

                case "get_serial": self.log(d.get_serial_number(), cmd)
                case "get_model": self.log(d.get_robot_model(), cmd)

                case "get_mode": self.log(d.get_operational_mode(), cmd)
                case "clear_mode": self.log(d.clear_operational_mode(), cmd)
                case "set_mode":
                    mode = getattr(OperationalModes, self.mode_select.value)
                    self.log(d.set_operational_mode(mode), cmd)

                case "set_role":
                    role = getattr(UserRoles, self.role_select.value)
                    self.log(d.set_user_role(role), cmd)

                case "in_remote": self.log(d.is_in_remote_control(), cmd)
                case "safety_status": self.log(d.get_safety_status(), cmd)
                case "close_safety": self.log(d.close_safety_popup(), cmd)
                case "restart_safety": self.log(d.restart_safety(), cmd)

                case "custom_cmd":
                    cmd_txt = self.custom_command_input.value
                    self.log(d.send_custom_dashboard_command(cmd_txt), cmd)

                case "get_var":
                    var = self.variable_input.value
                    response = d.get_variable(var)
                    # Gestion spéciale : variable non déclarée
                    if response.value.type.name == "None":
                        self.console.write(f"[yellow]Variable '{var}' not declared.")
                    else:
                        self.console.write(f"[green]{response.value.type.name} {response.value.name} = {response.value.value}")

        except Exception as e:
            self.console.write(f"[red]Exception: {str(e)}")

    # Loggue un résultat de commande avec succès ou échec
    def log(self, response, command):
        if response.succeed:
            self.console.write(f"[green]{command}() -> OK: {response}")
        else:
            self.console.write(f"[red]{command}() -> FAILED: {response}")
