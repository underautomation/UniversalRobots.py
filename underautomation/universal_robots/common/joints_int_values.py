from __future__ import annotations
import typing
from underautomation.universal_robots.common.joints_values_1 import JointsValues1
from UnderAutomation.UniversalRobots.Common import JointsIntValues as joints_int_values

class JointsIntValues(JointsValues1[int]):
	'''Represents a set of 6 integer values, one per robot joint. Typically used for joint modes, statuses, or other discrete joint data.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joints_int_values()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointsIntValues):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
