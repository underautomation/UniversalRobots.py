from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.rtde_value import RtdeValue
from UnderAutomation.UniversalRobots.Rtde import RtdeBaseValues as rtde_base_values

class RtdeBaseValues:
	'''Abstract base class holding a collection of RtdeValue instances representing RTDE variable values.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_base_values()
		else:
			self._instance = _internal

	@property
	def values(self) -> typing.List[RtdeValue]:
		'''Gets a copy of all RTDE values held by this instance.'''
		return [RtdeValue(x) for x in self._instance.Values]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeBaseValues):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
