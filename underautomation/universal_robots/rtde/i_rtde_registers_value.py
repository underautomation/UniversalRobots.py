from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Rtde import IRtdeRegistersValue as i_rtde_registers_value

class IRtdeRegistersValue:
	'''Interface for accessing individual register values within a register array by index.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_rtde_registers_value()
		else:
			self._instance = _internal

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
