from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.rtde_value import RtdeValue
from UnderAutomation.UniversalRobots.Rtde import RtdeValue as rtde_value_1

T = typing.TypeVar('T')
class RtdeValue1(RtdeValue, typing.Generic[T]):
	'''Strongly-typed RTDE variable value of type T.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_value_1()
		else:
			self._instance = _internal

	@property
	def value(self) -> T:
		'''Gets the current strongly-typed value.'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeValue1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
