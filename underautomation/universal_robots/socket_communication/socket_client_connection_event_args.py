from __future__ import annotations
import typing
from underautomation.universal_robots.socket_communication.socket_client import SocketClient
from UnderAutomation.UniversalRobots.SocketCommunication import SocketClientConnectionEventArgs as socket_client_connection_event_args

class SocketClientConnectionEventArgs:
	'''Event args raised when a socket client is connected with socket_open()'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = socket_client_connection_event_args()
		else:
			self._instance = _internal

	@property
	def client(self) -> SocketClient:
		'''Robot remote endpoint'''
		return SocketClient(self._instance.Client)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SocketClientConnectionEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
