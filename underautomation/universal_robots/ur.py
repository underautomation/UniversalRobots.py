from __future__ import annotations
import typing
from underautomation.universal_robots.internal.primary_interface_client_internal import PrimaryInterfaceClientInternal
from underautomation.universal_robots.internal.xml_rpc_server_internal import XmlRpcServerInternal
from underautomation.universal_robots.internal.dashboard_client_internal import DashboardClientInternal
from underautomation.universal_robots.internal.socket_communication_server_internal import SocketCommunicationServerInternal
from underautomation.universal_robots.internal.rtde_client_internal import RtdeClientInternal
from underautomation.universal_robots.internal.ssh_client_internal import SshClientInternal
from underautomation.universal_robots.internal.sftp_client_internal import SftpClientInternal
from underautomation.universal_robots.internal.interpreter_mode_client_internal import InterpreterModeClientInternal
from underautomation.universal_robots.internal.rest_client_internal import RestClientInternal
from underautomation.universal_robots.connect_parameters import ConnectParameters
from underautomation.universal_robots.license.license_info import LicenseInfo
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from UnderAutomation.UniversalRobots import UR as ur

class UR(URServiceBase):
	'''Main entry point for connecting to and interacting with a Universal Robots controller. Provides access to all communication interfaces: Primary Interface, Dashboard, RTDE, SSH, SFTP, XML-RPC, Socket Communication, Interpreter Mode, and REST API.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the UR class and creates all communication clients.'''
		if(_internal == 0):
			self._instance = ur()
		else:
			self._instance = _internal

	def connect(self, parameters: ConnectParameters) -> None:
		'''Connects to a robot with specific parameters

		:param parameters: Connection parameters
		'''
		self._instance.Connect(parameters._instance if parameters else None)

	def disconnect(self) -> None:
		'''Disconnects all clients and disable all services'''
		self._instance.Disconnect()

	@staticmethod
	def register_license(licensee: str, key: str) -> LicenseInfo:
		'''If you have a license and a key, please call this static method to register the product and exit the trial period You can register a product even if the trial period has ended

		:param licensee: Your organization name
		:param key: The associated key supplied by UnderAutomation
		:returns: Information about the supplied license
		'''
		return LicenseInfo(None, None, ur.RegisterLicense(licensee, key))

	@property
	def primary_interface(self) -> PrimaryInterfaceClientInternal:
		'''Interact with robot via Primary Interface'''
		return PrimaryInterfaceClientInternal(self._instance.PrimaryInterface)

	@property
	def xml_rpc(self) -> XmlRpcServerInternal:
		'''Interact with robot via XML-RPC'''
		return XmlRpcServerInternal(self._instance.XmlRpc)

	@property
	def dashboard(self) -> DashboardClientInternal:
		'''Interact with robot via Dashboard'''
		return DashboardClientInternal(self._instance.Dashboard)

	@property
	def socket_communication(self) -> SocketCommunicationServerInternal:
		'''Interact with robot via Socket communication'''
		return SocketCommunicationServerInternal(self._instance.SocketCommunication)

	@property
	def rtde(self) -> RtdeClientInternal:
		'''Interact with robot via RTDE'''
		return RtdeClientInternal(self._instance.Rtde)

	@property
	def ssh(self) -> SshClientInternal:
		'''Interact with robot via SSH'''
		return SshClientInternal(self._instance.Ssh)

	@property
	def sftp(self) -> SftpClientInternal:
		'''Interact with robot via SFTP'''
		return SftpClientInternal(self._instance.Sftp)

	@property
	def interpreter_mode(self) -> InterpreterModeClientInternal:
		'''Interact with robot via Interpreter Mode'''
		return InterpreterModeClientInternal(self._instance.InterpreterMode)

	@property
	def rest(self) -> RestClientInternal:
		'''Interact with robot via REST API (PolyscopeX only)'''
		return RestClientInternal(self._instance.Rest)

	@property
	def ip(self) -> str:
		'''Robot IP address, null is robot is disconnected'''
		return self._instance.IP

	@property
	def enabled(self) -> bool:
		'''Indicates that at least one of the implemented services is enabled'''
		return self._instance.Enabled

	@property
	def license_info(self) -> LicenseInfo:
		'''Return information about your license'''
		return LicenseInfo(None, None, self._instance.LicenseInfo)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UR):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
