from __future__ import annotations
import typing
from underautomation.universal_robots.socket_communication.internal.socket_communication_server_base import SocketCommunicationServerBase
from UnderAutomation.UniversalRobots.Internal import SocketCommunicationServerInternal as socket_communication_server_internal

class SocketCommunicationServerInternal(SocketCommunicationServerBase):
	'''Internal implementation of the socket communication server used for bidirectional data exchange with UR scripts.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = socket_communication_server_internal()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SocketCommunicationServerInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
