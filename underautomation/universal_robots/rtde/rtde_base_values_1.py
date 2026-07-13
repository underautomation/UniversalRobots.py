from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.rtde_base_values import RtdeBaseValues
from UnderAutomation.UniversalRobots.Rtde import RtdeBaseValues as rtde_base_values_1

T = typing.TypeVar('T')
class RtdeBaseValues1(RtdeBaseValues, typing.Generic[T]):
	'''Generic abstract base class for getting and setting RTDE variable values identified by enum T.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_base_values_1()
		else:
			self._instance = _internal

	def get_value(self, data: T, index: int) -> typing.Any:
		'''Gets the current value of the specified RTDE variable at a given register index.

		:param data: The RTDE variable identifier.
		:param index: The absolute register index.
		:returns: The current value at the given index.
		'''
		return self._instance.GetValue(data, index)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeBaseValues1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
