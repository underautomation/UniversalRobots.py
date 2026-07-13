from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.rtde_data_description_1 import RtdeDataDescription1
from underautomation.universal_robots.rtde.rtde_output_data import RtdeOutputData
from UnderAutomation.UniversalRobots.Rtde import RtdeOutputDataDescription as rtde_output_data_description
from UnderAutomation.UniversalRobots.Rtde import RtdeOutputData as rtde_output_data

class RtdeOutputDataDescription(RtdeDataDescription1[RtdeOutputData]):
	'''Describes a single RTDE output variable (robot-to-client), including its protocol name, type, and array information.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_output_data_description()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeOutputDataDescription):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
