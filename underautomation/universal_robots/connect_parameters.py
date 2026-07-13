from __future__ import annotations
import typing
from underautomation.universal_robots.common.primary_interface_connect_parameters import PrimaryInterfaceConnectParameters
from underautomation.universal_robots.common.dashboard_connect_parameters import DashboardConnectParameters
from underautomation.universal_robots.common.socket_communication_connect_parameters import SocketCommunicationConnectParameters
from underautomation.universal_robots.common.ssh_connect_parameters import SshConnectParameters
from underautomation.universal_robots.common.rtde_connect_parameters import RtdeConnectParameters
from underautomation.universal_robots.common.xml_rpc_connect_parameters import XmlRpcConnectParameters
from underautomation.universal_robots.common.interpreter_mode_connect_parameters import InterpreterModeConnectParameters
from underautomation.universal_robots.common.rest_connect_parameters import RestConnectParameters
from UnderAutomation.UniversalRobots import ConnectParameters as connect_parameters

class ConnectParameters:
	'''Contains parameters to connect to the robot'''
	def __init__(self, ip: str, _internal = 0):
		'''Initializes a new instance of ConnectParameters with the specified robot IP address.

		:param ip: The IP address of the Universal Robots controller.
		'''
		if(_internal == 0):
			self._instance = connect_parameters(ip)
		else:
			self._instance = _internal

	@property
	def ip(self) -> str:
		'''IP address of the Universal Robots controller.'''
		return self._instance.IP

	@ip.setter
	def ip(self, value: str):
		self._instance.IP = value

	@property
	def ping_before_connecting(self) -> bool:
		'''If true, a ping is sent to the robot before attempting connection. Default is true.'''
		return self._instance.PingBeforeConnecting

	@ping_before_connecting.setter
	def ping_before_connecting(self, value: bool):
		self._instance.PingBeforeConnecting = value

	@property
	def primary_interface(self) -> PrimaryInterfaceConnectParameters:
		'''Primary Interface connection parameters (port 30001/30002).'''
		return PrimaryInterfaceConnectParameters(self._instance.PrimaryInterface)

	@primary_interface.setter
	def primary_interface(self, value: PrimaryInterfaceConnectParameters):
		self._instance.PrimaryInterface = value._instance if value else None

	@property
	def dashboard(self) -> DashboardConnectParameters:
		'''Dashboard Server connection parameters (port 29999).'''
		return DashboardConnectParameters(self._instance.Dashboard)

	@dashboard.setter
	def dashboard(self, value: DashboardConnectParameters):
		self._instance.Dashboard = value._instance if value else None

	@property
	def socket_communication(self) -> SocketCommunicationConnectParameters:
		'''Socket communication connection parameters for exchanging data with URScript programs.'''
		return SocketCommunicationConnectParameters(self._instance.SocketCommunication)

	@socket_communication.setter
	def socket_communication(self, value: SocketCommunicationConnectParameters):
		self._instance.SocketCommunication = value._instance if value else None

	@property
	def ssh(self) -> SshConnectParameters:
		'''SSH and SFTP connection parameters for file transfer and remote shell access.'''
		return SshConnectParameters(self._instance.Ssh)

	@ssh.setter
	def ssh(self, value: SshConnectParameters):
		self._instance.Ssh = value._instance if value else None

	@property
	def rtde(self) -> RtdeConnectParameters:
		'''Real-Time Data Exchange (RTDE) connection parameters (port 30004).'''
		return RtdeConnectParameters(self._instance.Rtde)

	@rtde.setter
	def rtde(self, value: RtdeConnectParameters):
		self._instance.Rtde = value._instance if value else None

	@property
	def xml_rpc(self) -> XmlRpcConnectParameters:
		'''XML-RPC connection parameters for remote procedure calls.'''
		return XmlRpcConnectParameters(self._instance.XmlRpc)

	@xml_rpc.setter
	def xml_rpc(self, value: XmlRpcConnectParameters):
		self._instance.XmlRpc = value._instance if value else None

	@property
	def interpreter_mode(self) -> InterpreterModeConnectParameters:
		'''Interpreter Mode connection parameters for sending URScript lines interactively.'''
		return InterpreterModeConnectParameters(self._instance.InterpreterMode)

	@interpreter_mode.setter
	def interpreter_mode(self, value: InterpreterModeConnectParameters):
		self._instance.InterpreterMode = value._instance if value else None

	@property
	def rest(self) -> RestConnectParameters:
		'''REST API connection parameters (PolyscopeX only)'''
		return RestConnectParameters(self._instance.Rest)

	@rest.setter
	def rest(self, value: RestConnectParameters):
		self._instance.Rest = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
