from __future__ import annotations
import typing
from underautomation.universal_robots.socket_communication.socket_client import SocketClient
from UnderAutomation.UniversalRobots.SocketCommunication import SocketGetVarEventArgs as socket_get_var_event_args

class SocketGetVarEventArgs:
	'''Event args raised when a socket message sent with socket_get_var() is received'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = socket_get_var_event_args()
		else:
			self._instance = _internal

	@property
	def client(self) -> SocketClient:
		'''Robot remote endpoint'''
		return SocketClient(self._instance.Client)

	@property
	def name(self) -> str:
		'''Name of requested variable'''
		return self._instance.Name

	@property
	def value(self) -> int | None:
		'''Variable value to send to the robot. If value is null, no messsage is replied to the robot'''
		return self._instance.Value

	@value.setter
	def value(self, value: int | None):
		self._instance.Value = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SocketGetVarEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
