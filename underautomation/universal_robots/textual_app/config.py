import json
import os

# Modèle de données pour stocker les informations de configuration
class ConfigData:
    def __init__(self, licensee="", key="", ur_script="", ip_address="127.0.0.1"):
        self.licensee = licensee         # Nom du titulaire de la licence
        self.key = key                   # Clé de licence
        self.ur_script = ur_script       # Dernier script UR utilisé
        self.ip_address = ip_address     # Adresse IP du robot (configurable)

    def to_dict(self):
        # Convertit les données en dictionnaire pour sérialisation JSON
        return {
            "licensee": self.licensee,
            "key": self.key,
            "ur_script": self.ur_script,
            "ip_address": self.ip_address
        }

    @staticmethod
    def from_dict(data: dict):
        # Crée une instance à partir d’un dictionnaire (ex: depuis un fichier JSON)
        return ConfigData(
            licensee=data.get("licensee", ""),
            key=data.get("key", ""),
            ur_script=data.get("ur_script", ""),
            ip_address=data.get("ip_address", "127.0.0.1")
        )


# Gestionnaire de configuration principal (singleton)
class Config:
    current = ConfigData()  # Instance courante de la configuration

    @staticmethod
    def load():
        # Charge les données de configuration depuis un fichier JSON
        if os.path.exists(CONFIG_PATH):
            try:
                with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    Config.current = ConfigData.from_dict(data)
            except Exception as e:
                print(f"Erreur lors du chargement de la configuration : {e}")

    @staticmethod
    def save():
        # Sauvegarde la configuration courante dans un fichier JSON
        try:
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                json.dump(Config.current.to_dict(), f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de la configuration : {e}")


# Définition du chemin de configuration (fichier `config.json` dans le dossier utilisateur)
CONFIG_PATH = os.path.join(os.path.expanduser("~"), "ur_config.json")
