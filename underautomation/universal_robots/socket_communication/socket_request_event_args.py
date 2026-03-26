import typing
from __future__ import annotation
from underautomation.universal_robots.socket_communication.socket_client import SocketClient
from UnderAutomation.UniversalRobots.SocketCommunication import SocketRequestEventArgs as socket_request_event_args

class SocketRequestEventArgs:
	'''Event args raised when a socket message is received'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = socket_request_event_args()
		else:
			self._instance = _internal

	@property
	def message(self) -> str:
		'''Message content received from robot'''
		return self._instance.Message

	@property
	def client(self) -> SocketClient:
		'''Robot IP information'''
		return SocketClient(self._instance.Client)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SocketRequestEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
