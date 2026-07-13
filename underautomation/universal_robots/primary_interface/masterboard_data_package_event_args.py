from __future__ import annotations
import typing
from underautomation.universal_robots.common.analog_ranges import AnalogRanges
from underautomation.universal_robots.common.safety_status import SafetyStatus
from underautomation.universal_robots.primary_interface.masterboard_digital_io import MasterboardDigitalIO
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import MasterboardDataPackageEventArgs as masterboard_data_package_event_args
from UnderAutomation.UniversalRobots.Common import AnalogRanges as analog_ranges
from UnderAutomation.UniversalRobots.Common import SafetyStatus as safety_status

class MasterboardDataPackageEventArgs(PackageEventArgs):
	'''Masterboard data'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = masterboard_data_package_event_args()
		else:
			self._instance = _internal

	@property
	def analog_input_range0(self) -> AnalogRanges:
		'''Unit of analog input 0 (analog_in[0])'''
		return AnalogRanges(int(self._instance.AnalogInputRange0))

	@analog_input_range0.setter
	def analog_input_range0(self, value: AnalogRanges):
		self._instance.AnalogInputRange0 = analog_ranges(int(value))

	@property
	def analog_input_range1(self) -> AnalogRanges:
		'''Unit of analog input 1 (analog_in[1])'''
		return AnalogRanges(int(self._instance.AnalogInputRange1))

	@analog_input_range1.setter
	def analog_input_range1(self, value: AnalogRanges):
		self._instance.AnalogInputRange1 = analog_ranges(int(value))

	@property
	def analog_input0(self) -> float:
		'''Value of analog input 0 (analog_in[0])'''
		return self._instance.AnalogInput0

	@analog_input0.setter
	def analog_input0(self, value: float):
		self._instance.AnalogInput0 = value

	@property
	def analog_input1(self) -> float:
		'''Value of analog input 1 (analog_in[1])'''
		return self._instance.AnalogInput1

	@analog_input1.setter
	def analog_input1(self, value: float):
		self._instance.AnalogInput1 = value

	@property
	def analog_output_domain0(self) -> AnalogRanges:
		'''Unit of analog output 0 (analog_out[0])'''
		return AnalogRanges(int(self._instance.AnalogOutputDomain0))

	@analog_output_domain0.setter
	def analog_output_domain0(self, value: AnalogRanges):
		self._instance.AnalogOutputDomain0 = analog_ranges(int(value))

	@property
	def analog_output_domain1(self) -> AnalogRanges:
		'''Unit of analog output 1 (analog_out[1])'''
		return AnalogRanges(int(self._instance.AnalogOutputDomain1))

	@analog_output_domain1.setter
	def analog_output_domain1(self, value: AnalogRanges):
		self._instance.AnalogOutputDomain1 = analog_ranges(int(value))

	@property
	def analog_output0(self) -> float:
		'''Value of analog output 0 (analog_out[0])'''
		return self._instance.AnalogOutput0

	@analog_output0.setter
	def analog_output0(self, value: float):
		self._instance.AnalogOutput0 = value

	@property
	def analog_output1(self) -> float:
		'''Value of analog output 1 (analog_out[1])'''
		return self._instance.AnalogOutput1

	@analog_output1.setter
	def analog_output1(self, value: float):
		self._instance.AnalogOutput1 = value

	@property
	def masterboard_temperature(self) -> float:
		'''Temperature of masterboard in °C'''
		return self._instance.MasterboardTemperature

	@masterboard_temperature.setter
	def masterboard_temperature(self, value: float):
		self._instance.MasterboardTemperature = value

	@property
	def robot_voltage48_v(self) -> float:
		'''Voltage of internal 48V power supply'''
		return self._instance.RobotVoltage48V

	@robot_voltage48_v.setter
	def robot_voltage48_v(self, value: float):
		self._instance.RobotVoltage48V = value

	@property
	def robot_current(self) -> float:
		'''Robot current consumption in Amps'''
		return self._instance.RobotCurrent

	@robot_current.setter
	def robot_current(self, value: float):
		self._instance.RobotCurrent = value

	@property
	def master_io_current(self) -> float:
		'''Current of all digital and analog inputs and outputs'''
		return self._instance.MasterIOCurrent

	@master_io_current.setter
	def master_io_current(self, value: float):
		self._instance.MasterIOCurrent = value

	@property
	def safetymode(self) -> SafetyStatus:
		'''Masterboard safety mode'''
		return SafetyStatus(int(self._instance.Safetymode))

	@safetymode.setter
	def safetymode(self, value: SafetyStatus):
		self._instance.Safetymode = safety_status(int(value))

	@property
	def in_reduced_mode(self) -> int:
		'''Robot is in reduced speed mode'''
		return self._instance.InReducedMode

	@in_reduced_mode.setter
	def in_reduced_mode(self, value: int):
		self._instance.InReducedMode = value

	@property
	def operational_mode_selector_input(self) -> int:
		'''Position of operational mode selector input switch'''
		return self._instance.OperationalModeSelectorInput

	@operational_mode_selector_input.setter
	def operational_mode_selector_input(self, value: int):
		self._instance.OperationalModeSelectorInput = value

	@property
	def three_position_enabling_device_input(self) -> int:
		'''Position of the 3-position enabling device'''
		return self._instance.ThreePositionEnablingDeviceInput

	@three_position_enabling_device_input.setter
	def three_position_enabling_device_input(self, value: int):
		self._instance.ThreePositionEnablingDeviceInput = value

	@property
	def digital_inputs(self) -> MasterboardDigitalIO:
		'''Register where each bit is a digital input value'''
		return MasterboardDigitalIO(self._instance.DigitalInputs)

	@digital_inputs.setter
	def digital_inputs(self, value: MasterboardDigitalIO):
		self._instance.DigitalInputs = value._instance if value else None

	@property
	def digital_outputs(self) -> MasterboardDigitalIO:
		'''Register where each bit is a digital output value'''
		return MasterboardDigitalIO(self._instance.DigitalOutputs)

	@digital_outputs.setter
	def digital_outputs(self, value: MasterboardDigitalIO):
		self._instance.DigitalOutputs = value._instance if value else None

	@property
	def euromap67_installed(self) -> int:
		'''The robot is interfaced to injection molding machines Euromap 67'''
		return self._instance.Euromap67Installed

	@euromap67_installed.setter
	def euromap67_installed(self, value: int):
		self._instance.Euromap67Installed = value

	@property
	def euromap_input_bits(self) -> int:
		'''Register where each bit is a digital Euromap input'''
		return self._instance.EuromapInputBits

	@euromap_input_bits.setter
	def euromap_input_bits(self, value: int):
		self._instance.EuromapInputBits = value

	@property
	def euromap_output_bits(self) -> int:
		'''Register where each bit is a digital Euromap output'''
		return self._instance.EuromapOutputBits

	@euromap_output_bits.setter
	def euromap_output_bits(self, value: int):
		self._instance.EuromapOutputBits = value

	@property
	def euromap_voltage(self) -> float:
		'''Euromap voltage'''
		return self._instance.EuromapVoltage

	@euromap_voltage.setter
	def euromap_voltage(self, value: float):
		self._instance.EuromapVoltage = value

	@property
	def euromap_current(self) -> float:
		'''Euromap current'''
		return self._instance.EuromapCurrent

	@euromap_current.setter
	def euromap_current(self, value: float):
		self._instance.EuromapCurrent = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MasterboardDataPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
