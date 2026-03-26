import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Rtde import IRtdeRegistersValue as i_rtde_registers_value

class IRtdeRegistersValue:
	'''Interface for accessing individual register values within a register array by index.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_rtde_registers_value()
		else:
			self._instance = _internal

	def get_value(self, index: int) -> typing.Any:
		'''Gets the value at the specified register index.

		:param index: The absolute register index.
		:returns: The value stored at the given index.
		'''
		return self._instance.GetValue(index)

	def set_value(self, index: int, value: typing.Any) -> None:
		'''Sets the value at the specified register index.

		:param index: The absolute register index.
		:param value: The value to store.
		'''
		self._instance.SetValue(index, value)

	@property
	def lower_range_index(self) -> int:
		'''Gets the lower-bound register index for this register range.'''
		return self._instance.LowerRangeIndex

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IRtdeRegistersValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
