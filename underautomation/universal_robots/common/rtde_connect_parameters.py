from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.internal.rtde_parameters_base import RtdeParametersBase
from UnderAutomation.UniversalRobots.Common import RtdeConnectParameters as rtde_connect_parameters

class RtdeConnectParameters(RtdeParametersBase):
	'''Setup RTDE (Real-Time Data Exchange) client communication'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Choose to enable RTDE (Real-Time Data Exchange) Default value is false'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
