from __future__ import annotations
import typing
from underautomation.universal_robots.common.analog_ranges import AnalogRanges
from underautomation.universal_robots.common.tool_modes import ToolModes
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import ToolDataPackageEventArgs as tool_data_package_event_args
from UnderAutomation.UniversalRobots.Common import AnalogRanges as analog_ranges
from UnderAutomation.UniversalRobots.Common import ToolModes as tool_modes

class ToolDataPackageEventArgs(PackageEventArgs):
	'''Tool data'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tool_data_package_event_args()
		else:
			self._instance = _internal

	@property
	def analog_input_range2(self) -> AnalogRanges:
		'''Unit of analog input 2 (analog_in[2])'''
		return AnalogRanges(int(self._instance.AnalogInputRange2))

	@analog_input_range2.setter
	def analog_input_range2(self, value: AnalogRanges):
		self._instance.AnalogInputRange2 = analog_ranges(int(value))

	@property
	def analog_input_range3(self) -> AnalogRanges:
		'''Unit of analog input 3 (analog_in[3])'''
		return AnalogRanges(int(self._instance.AnalogInputRange3))

	@analog_input_range3.setter
	def analog_input_range3(self, value: AnalogRanges):
		self._instance.AnalogInputRange3 = analog_ranges(int(value))

	@property
	def analog_input2(self) -> float:
		'''Value of Analog input 2 (analog_in[2])'''
		return self._instance.AnalogInput2

	@analog_input2.setter
	def analog_input2(self, value: float):
		self._instance.AnalogInput2 = value

	@property
	def analog_input3(self) -> float:
		'''Value of Analog input 3 (analog_in[3])'''
		return self._instance.AnalogInput3

	@analog_input3.setter
	def analog_input3(self, value: float):
		self._instance.AnalogInput3 = value

	@property
	def tool_voltage48_v(self) -> float:
		'''Actual robot voltage power supply'''
		return self._instance.ToolVoltage48V

	@tool_voltage48_v.setter
	def tool_voltage48_v(self, value: float):
		self._instance.ToolVoltage48V = value

	@property
	def tool_output_voltage(self) -> int:
		'''Tool output voltage'''
		return self._instance.ToolOutputVoltage

	@tool_output_voltage.setter
	def tool_output_voltage(self, value: int):
		self._instance.ToolOutputVoltage = value

	@property
	def tool_current(self) -> float:
		'''Tool current in Amps'''
		return self._instance.ToolCurrent

	@tool_current.setter
	def tool_current(self, value: float):
		self._instance.ToolCurrent = value

	@property
	def tool_temperature(self) -> float:
		'''Tool Temperature in °C'''
		return self._instance.ToolTemperature

	@tool_temperature.setter
	def tool_temperature(self, value: float):
		self._instance.ToolTemperature = value

	@property
	def tool_mode(self) -> ToolModes:
		'''Tool mode'''
		return ToolModes(int(self._instance.ToolMode))

	@tool_mode.setter
	def tool_mode(self, value: ToolModes):
		self._instance.ToolMode = tool_modes(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ToolDataPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
