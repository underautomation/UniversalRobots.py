from __future__ import annotations
import typing
from underautomation.universal_robots.socket_communication.internal.socket_communication_parameters_base import SocketCommunicationParametersBase
from UnderAutomation.UniversalRobots.Common import SocketCommunicationConnectParameters as socket_communication_connect_parameters

class SocketCommunicationConnectParameters(SocketCommunicationParametersBase):
	'''Setup socket communication server'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = socket_communication_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Choose to enable socket communication server Default value is false'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SocketCommunicationConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
