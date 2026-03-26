import typing
from __future__ import annotation
from underautomation.universal_robots.rtde.i_rtde_registers_value import IRtdeRegistersValue
from underautomation.universal_robots.rtde.rtde_value_1 import RtdeValue1
from UnderAutomation.UniversalRobots.Rtde import RtdeRegistersValue as rtde_registers_value_1

T = typing.TypeVar('T')
class RtdeRegistersValue1(RtdeValue1[typing.List[T]], IRtdeRegistersValue, typing.Generic[T]):
	'''Abstract base for a fixed-size register array of type T exchanged through RTDE.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_registers_value_1()
		else:
			self._instance = _internal

	def set_value(self, index: int, value: T) -> None:
		'''Sets the value at the specified absolute register index.

		:param index: The absolute register index.
		:param value: The value to store.
		'''
		self._instance.SetValue(index, value)

	def get_value(self, index: int) -> T:
		'''Gets the value at the specified absolute register index.

		:param index: The absolute register index.
		:returns: The value stored at the given index.
		'''
		return self._instance.GetValue(index)

	@property
	def lower_range_index(self) -> int:
		'''Gets the lower-bound register index for this register range.'''
		return self._instance.LowerRangeIndex

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeRegistersValue1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
