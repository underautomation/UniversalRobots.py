from textual.app import App
from textual.widgets import Button, Static

class Sidebar(App):
    async def on_mount(self):
        # Créer un en-tête statique
        self.header = Static("Menu Principal", id="menu-title")

        # Ajouter des boutons avec des identifiants uniques
        self.connection_btn = Button("Connection", id="nav-btn-connection")
        self.primaryinterface_btn = Button("Primary Interface", id="nav-btn-primaryinterface")  # <-- AJOUT ICI
        self.dashboard_btn = Button("Dashboard", id="nav-btn-dashboard")
        self.rtde_btn = Button("RTDE", id="nav-btn-rtde")
        self.sftp_btn = Button("SFTP", id="nav-btn-sftp")
        self.runningprogram_btn = Button("Running Program", id="nav-btn-runningprogram")
        self.variables_btn = Button("Variables", id="nav-btn-variables")
        self.license_btn = Button("License", id="nav-btn-license")

        # Montez tous les widgets
        await self.mount(
            self.header,
            self.connection_btn,
            self.primaryinterface_btn,  
            self.dashboard_btn,
            self.rtde_btn,
            self.sftp_btn,
            self.runningprogram_btn,
            self.variables_btn,
            self.license_btn
        )

    async def on_button_pressed(self, message: Button.Pressed) -> None:
        if message.button.id == "nav-btn-connection":
            print("Connection pressed")
        elif message.button.id == "nav-btn-primaryinterface":  
            print("Primary Interface pressed")
        elif message.button.id == "nav-btn-dashboard":
            print("Dashboard pressed")
        elif message.button.id == "nav-btn-rtde":
            print("RTDE pressed")
        elif message.button.id == "nav-btn-sftp":
            print("SFTP pressed")
        elif message.button.id == "nav-btn-runningprogram":
            print("Running Program pressed")
        elif message.button.id == "nav-btn-variables":
            print("Variables pressed")
        elif message.button.id == "nav-btn-license":
            print("License pressed")

if __name__ == "__main__":
    Sidebar().run()
