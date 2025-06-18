# ur.py

# Classes simulées pour les clients internes, servant de stubs ou mocks
# afin de faciliter le développement sans accès au vrai matériel ou API.

class DashboardClientInternal:
    def __init__(self, dashboard_impl):
        self._impl = dashboard_impl

    def status(self):
        # Retourne un statut simulé du dashboard
        return f"Statut Dashboard: {self._impl}"


class PrimaryInterfaceClientInternal:
    def __init__(self, primary_impl):
        self._impl = primary_impl
        # Callbacks simulées pour réception de messages
        self.popup_message_received = None
        self.runtime_exception_message_received = None

    def send(self, script: str):
        # Simule l'envoi d'un script à l'interface primaire
        print(f"Script envoyé : {script}")
        # Simule réception d'un popup message
        if self.popup_message_received:
            self.popup_message_received(self, "Popup simulé")
        # Simule réception d'une exception runtime
        if self.runtime_exception_message_received:
            self.runtime_exception_message_received(self, "Exception runtime simulée")


class XmlRpcServerInternal:
    def __init__(self, xmlrpc_impl):
        self._impl = xmlrpc_impl
        # Peut être étendu avec des méthodes simulant le serveur XML-RPC


class RtdeClientInternal:
    def __init__(self, rtde_impl):
        self._impl = rtde_impl
        # Peut contenir des méthodes simulant la communication RTDE


class SftpClientInternal:
    def __init__(self, sftp_impl):
        self._impl = sftp_impl
        # Peut contenir des méthodes simulant les opérations SFTP


class LicenseInfo:
    def __init__(self, valid, holder, raw_info=None):
        self.valid = valid          # Booléen indiquant si la licence est valide
        self.holder = holder        # Nom du titulaire de la licence
        self.raw_info = raw_info    # Informations brutes complémentaires (optionnel)


# Classe simulée représentant la connexion universelle au robot UR
class UniversalRobots:
    def __init__(self, ip):
        self.ip = ip
        # Stocke des chaînes simulant les implémentations internes
        self.Dashboard = f"Dashboard impl for {ip}"
        self.PrimaryInterface = f"Primary interface impl for {ip}"
        self.XmlRpc = f"XmlRpc impl for {ip}"
        self.RTDE = f"RTDE impl for {ip}"
        self.SFTP = f"SFTP impl for {ip}"


# Classe principale exposée à l'application, qui encapsule l'instance simulée
class UR:
    def __init__(self, ip: str):
        self._instance = UniversalRobots(ip)
        self.ip = ip

    @property
    def dashboard(self) -> DashboardClientInternal:
        # Accès au client dashboard simulé
        return DashboardClientInternal(self._instance.Dashboard)

    @property
    def primary_interface(self) -> PrimaryInterfaceClientInternal:
        # Accès au client interface primaire simulé
        return PrimaryInterfaceClientInternal(self._instance.PrimaryInterface)

    @property
    def xml_rpc(self) -> XmlRpcServerInternal:
        # Accès au serveur XML-RPC simulé
        return XmlRpcServerInternal(self._instance.XmlRpc)

    @property
    def rtde(self) -> RtdeClientInternal:
        # Accès au client RTDE simulé
        return RtdeClientInternal(self._instance.RTDE)

    @property
    def sftp(self) -> SftpClientInternal:
        # Accès au client SFTP simulé
        return SftpClientInternal(self._instance.SFTP)

    @staticmethod
    def register_license(licensee: str, key: str):
        # Simule l'enregistrement d'une licence avec licensee et clé
        print(f"Licence enregistrée pour {licensee} avec clé {key}")

    @staticmethod
    def license_info() -> LicenseInfo:
        # Simule la récupération des informations de licence
        return LicenseInfo(True, "Utilisateur simulé")
