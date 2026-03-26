import typing
from __future__ import annotation
from underautomation.universal_robots.socket_communication.internal.socket_communication_server_base import SocketCommunicationServerBase
from UnderAutomation.UniversalRobots.SocketCommunication import SocketCommunicationServer as socket_communication_server

class SocketCommunicationServer(SocketCommunicationServerBase):
	'''Represents a Socket Communication server to which the robot can connect'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = socket_communication_server()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SocketCommunicationServer):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
