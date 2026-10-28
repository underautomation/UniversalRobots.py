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

class _StaticProperty:
	'''Property of the class, readable from the class or from an instance'''
	def __init__(self, fget, fset=None):
		self._fget = fget
		self._fset = fset
		self.__doc__ = fget.__doc__

	def __get__(self, obj, owner=None):
		return self._fget()

	def __set__(self, obj, value):
		if self._fset is None:
			raise AttributeError("read-only property")
		self._fset(value)

class UR(URServiceBase):
	'''Main entry point for connecting to and interacting with a Universal Robots controller. Provides access to all communication interfaces: Primary Interface, Dashboard, RTDE, SSH, SFTP, XML-RPC, Socket Communication, Interpreter Mode, and REST API.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the UR class and creates all communication clients.'''
		if(_internal == 0):
			self._instance = ur()
		else:
			self._instance = _internal

	def connect(self, ip_or_parameters: str | ConnectParameters) -> None:
		'''Connects to a robot with default parameters
		Connects to a robot with specific parameters

		:param ip_or_parameters: Robot IP address. Or: Connection parameters.
		'''
		self._instance.Connect(getattr(ip_or_parameters, '_instance', ip_or_parameters))

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
		__r = ur.RegisterLicense(licensee, key)
		return None if __r is None else LicenseInfo(None, None, __r)

	@property
	def primary_interface(self) -> PrimaryInterfaceClientInternal:
		'''Interact with robot via Primary Interface'''
		__r = self._instance.PrimaryInterface
		return None if __r is None else PrimaryInterfaceClientInternal(__r)

	@property
	def xml_rpc(self) -> XmlRpcServerInternal:
		'''Interact with robot via XML-RPC'''
		__r = self._instance.XmlRpc
		return None if __r is None else XmlRpcServerInternal(__r)

	@property
	def dashboard(self) -> DashboardClientInternal:
		'''Interact with robot via Dashboard'''
		__r = self._instance.Dashboard
		return None if __r is None else DashboardClientInternal(__r)

	@property
	def socket_communication(self) -> SocketCommunicationServerInternal:
		'''Interact with robot via Socket communication'''
		__r = self._instance.SocketCommunication
		return None if __r is None else SocketCommunicationServerInternal(__r)

	@property
	def rtde(self) -> RtdeClientInternal:
		'''Interact with robot via RTDE'''
		__r = self._instance.Rtde
		return None if __r is None else RtdeClientInternal(__r)

	@property
	def ssh(self) -> SshClientInternal:
		'''Interact with robot via SSH'''
		__r = self._instance.Ssh
		return None if __r is None else SshClientInternal(__r)

	@property
	def sftp(self) -> SftpClientInternal:
		'''Interact with robot via SFTP'''
		__r = self._instance.Sftp
		return None if __r is None else SftpClientInternal(__r)

	@property
	def interpreter_mode(self) -> InterpreterModeClientInternal:
		'''Interact with robot via Interpreter Mode'''
		__r = self._instance.InterpreterMode
		return None if __r is None else InterpreterModeClientInternal(__r)

	@property
	def rest(self) -> RestClientInternal:
		'''Interact with robot via REST API (PolyscopeX only)'''
		__r = self._instance.Rest
		return None if __r is None else RestClientInternal(__r)

	@property
	def ip(self) -> str:
		'''Robot IP address, null is robot is disconnected'''
		return self._instance.IP

	@property
	def enabled(self) -> bool:
		'''Indicates that at least one of the implemented services is enabled'''
		return self._instance.Enabled

	@staticmethod
	def _get_license_info() -> LicenseInfo:
		'''Return information about your license'''
		__r = ur.LicenseInfo
		return None if __r is None else LicenseInfo(None, None, __r)

	license_info = _StaticProperty(_get_license_info)
	del _get_license_info

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
