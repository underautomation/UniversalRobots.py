from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.SocketCommunication.Internal import SocketCommunicationParametersBase as socket_communication_parameters_base

class SocketCommunicationParametersBase:
	'''Base parameters for socket communication server configuration'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = socket_communication_parameters_base()
		else:
			self._instance = _internal

	@property
	def port(self) -> int:
		'''Local port for socket server (default : 50001)'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SocketCommunicationParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
