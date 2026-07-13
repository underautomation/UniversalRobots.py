from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.rtde_data_description_1 import RtdeDataDescription1
from underautomation.universal_robots.rtde.rtde_input_data import RtdeInputData
from UnderAutomation.UniversalRobots.Rtde import RtdeInputDataDescription as rtde_input_data_description
from UnderAutomation.UniversalRobots.Rtde import RtdeInputData as rtde_input_data

class RtdeInputDataDescription(RtdeDataDescription1[RtdeInputData]):
	'''Describes a single RTDE input variable (client-to-robot), including its protocol name, type, and array information.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_input_data_description()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeInputDataDescription):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
