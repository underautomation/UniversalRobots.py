from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Rtde import RtdeClientParameters as rtde_client_parameters

class RtdeClientParameters:
	'''Parameters for configuring the standalone RtdeClient connection to a Universal Robots controller via the RTDE protocol.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_client_parameters()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeClientParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
