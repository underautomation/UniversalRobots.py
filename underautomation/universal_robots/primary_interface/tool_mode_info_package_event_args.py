import typing
from __future__ import annotation
from underautomation.universal_robots.common.output_modes import OutputModes
from underautomation.universal_robots.common.digital_output_configurations import DigitalOutputConfigurations
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import ToolModeInfoPackageEventArgs as tool_mode_info_package_event_args
from UnderAutomation.UniversalRobots.Common import OutputModes as output_modes
from UnderAutomation.UniversalRobots.Common import DigitalOutputConfigurations as digital_output_configurations

class ToolModeInfoPackageEventArgs(PackageEventArgs):
	'''Tool mode info'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tool_mode_info_package_event_args()
		else:
			self._instance = _internal

	@property
	def output_mode(self) -> OutputModes:
		'''Digital output mode'''
		return OutputModes(int(self._instance.OutputMode))

	@output_mode.setter
	def output_mode(self, value: OutputModes):
		self._instance.OutputMode = output_modes(int(value))

	@property
	def digital_output_mode0(self) -> DigitalOutputConfigurations:
		'''Digital output 0 configuration'''
		return DigitalOutputConfigurations(int(self._instance.DigitalOutputMode0))

	@digital_output_mode0.setter
	def digital_output_mode0(self, value: DigitalOutputConfigurations):
		self._instance.DigitalOutputMode0 = digital_output_configurations(int(value))

	@property
	def digital_output_mode1(self) -> DigitalOutputConfigurations:
		'''Digital output 1 configuration'''
		return DigitalOutputConfigurations(int(self._instance.DigitalOutputMode1))

	@digital_output_mode1.setter
	def digital_output_mode1(self, value: DigitalOutputConfigurations):
		self._instance.DigitalOutputMode1 = digital_output_configurations(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ToolModeInfoPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
