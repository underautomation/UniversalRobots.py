from __future__ import annotations
import typing
from underautomation.universal_robots.common.joints_values_1 import JointsValues1
from UnderAutomation.UniversalRobots.Common import JointsDoubleValues as joints_double_values

class JointsDoubleValues(JointsValues1[float]):
	'''Represents a set of 6 double-precision values, one per robot joint. Typically used for angles (radians), velocities, currents, etc.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joints_double_values()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointsDoubleValues):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
