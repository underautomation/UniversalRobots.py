import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rtde import IRtdeRegistersValue as i_rtde_registers_value

class IRtdeRegistersValue:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_rtde_registers_value()
		else:
			self._instance = _internal
	def get_value(self, index: int) -> typing.Any:
		return self._instance.GetValue(index)
	def set_value(self, index: int, value: typing.Any) -> None:
		self._instance.SetValue(index, value)
	@property
	def lower_range_index(self) -> int:
		return self._instance.LowerRangeIndex
