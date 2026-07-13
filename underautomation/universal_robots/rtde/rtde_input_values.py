from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.rtde_input_setup_item import RtdeInputSetupItem
from underautomation.universal_robots.rtde.rtde_input_data import RtdeInputData
from underautomation.universal_robots.rtde.rtde_bit_registers_value import RtdeBitRegistersValue
from underautomation.universal_robots.rtde.rtde_int_registers_value import RtdeIntRegistersValue
from underautomation.universal_robots.rtde.rtde_double_registers_value import RtdeDoubleRegistersValue
from underautomation.universal_robots.common.cartesian_coordinates import CartesianCoordinates
from underautomation.universal_robots.rtde.rtde_base_values_1 import RtdeBaseValues1
from UnderAutomation.UniversalRobots.Rtde import RtdeInputValues as rtde_input_values
from UnderAutomation.UniversalRobots.Rtde import RtdeInputData as rtde_input_data

class RtdeInputValues(RtdeBaseValues1[RtdeInputData]):
	'''Holds the current values for all RTDE input variables (client-to-robot). Use this to prepare data before calling RtdeInputValues).'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance with default values for all input variables.'''
		if(_internal == 0):
			self._instance = rtde_input_values()
		else:
			self._instance = _internal

	def set_value(self, data: RtdeInputData, index: int, value: typing.Any) -> None:
		'''Sets the value for the specified RTDE input variable at a given register index.

		:param data: The input variable identifier.
		:param index: The absolute register index.
		:param value: The value to assign.
		'''
		self._instance.SetValue(rtde_input_data(int(data)), index, value)

	def get_value(self, item: RtdeInputSetupItem) -> typing.Any:
		'''Gets the current value for the input variable described by a setup item.

		:param item: The input setup item identifying the variable and register index.
		:returns: The current value.
		'''
		return self._instance.GetValue(item._instance if item else None)

	def reset(self) -> None:
		'''Resets all input values to their defaults.'''
		self._instance.Reset()

	@property
	def speed_slider_mask(self) -> int:
		'''0 = don't change speed slider with this input, 1 = use speed_slider_fraction to set speed slider value'''
		return self._instance.SpeedSliderMask

	@speed_slider_mask.setter
	def speed_slider_mask(self, value: int):
		self._instance.SpeedSliderMask = value

	@property
	def speed_slider_fraction(self) -> float:
		'''new speed slider value'''
		return self._instance.SpeedSliderFraction

	@speed_slider_fraction.setter
	def speed_slider_fraction(self, value: float):
		self._instance.SpeedSliderFraction = value

	@property
	def standard_digital_output_mask(self) -> int:
		'''Standard digital output bit mask'''
		return self._instance.StandardDigitalOutputMask

	@standard_digital_output_mask.setter
	def standard_digital_output_mask(self, value: int):
		self._instance.StandardDigitalOutputMask = value

	@property
	def configurable_digital_output_mask(self) -> int:
		'''Configurable digital output bit mask'''
		return self._instance.ConfigurableDigitalOutputMask

	@configurable_digital_output_mask.setter
	def configurable_digital_output_mask(self, value: int):
		self._instance.ConfigurableDigitalOutputMask = value

	@property
	def standard_digital_output(self) -> int:
		'''Standard digital outputs'''
		return self._instance.StandardDigitalOutput

	@standard_digital_output.setter
	def standard_digital_output(self, value: int):
		self._instance.StandardDigitalOutput = value

	@property
	def configurable_digital_output(self) -> int:
		'''Configurable digital outputs'''
		return self._instance.ConfigurableDigitalOutput

	@configurable_digital_output.setter
	def configurable_digital_output(self, value: int):
		self._instance.ConfigurableDigitalOutput = value

	@property
	def standard_analog_output_mask(self) -> int:
		'''Standard analog output mask'''
		return self._instance.StandardAnalogOutputMask

	@standard_analog_output_mask.setter
	def standard_analog_output_mask(self, value: int):
		self._instance.StandardAnalogOutputMask = value

	@property
	def standard_analog_output_type(self) -> int:
		'''Output domain {0=current[mA], 1=voltage[V]}. Bits 0-1: standard_analog_output_0 | standard_analog_output_1'''
		return self._instance.StandardAnalogOutputType

	@standard_analog_output_type.setter
	def standard_analog_output_type(self, value: int):
		self._instance.StandardAnalogOutputType = value

	@property
	def standard_analog_output0(self) -> float:
		'''Standard analog output 0 (ratio) [0..1]'''
		return self._instance.StandardAnalogOutput0

	@standard_analog_output0.setter
	def standard_analog_output0(self, value: float):
		self._instance.StandardAnalogOutput0 = value

	@property
	def standard_analog_output1(self) -> float:
		'''Standard analog output 1 (ratio) [0..1]'''
		return self._instance.StandardAnalogOutput1

	@standard_analog_output1.setter
	def standard_analog_output1(self, value: float):
		self._instance.StandardAnalogOutput1 = value

	@property
	def input_bt_registers0_to31(self) -> int:
		'''General purpose bits. This range of the boolean input registers is reserved for FieldBus/PLC interface usage.'''
		return self._instance.InputBtRegisters0To31

	@input_bt_registers0_to31.setter
	def input_bt_registers0_to31(self, value: int):
		self._instance.InputBtRegisters0To31 = value

	@property
	def input_bt_registers32_to63(self) -> int:
		'''General purpose bits. This range of the boolean input registers is reserved for FieldBus/PLC interface usage.'''
		return self._instance.InputBtRegisters32To63

	@input_bt_registers32_to63.setter
	def input_bt_registers32_to63(self, value: int):
		self._instance.InputBtRegisters32To63 = value

	@property
	def input_bit_registers(self) -> RtdeBitRegistersValue:
		'''64 general purpose bits. X: [64..127] - The upper range of the boolean input registers can be used by external RTDE clients (i.e URCAPS).'''
		return RtdeBitRegistersValue(self._instance.InputBitRegisters)

	@property
	def input_int_registers(self) -> RtdeIntRegistersValue:
		'''48 general purpose integer registers. X: [0..23] - The lower range of the integer input registers is reserved for FieldBus/PLC interface usage. X: [24..47] - The upper range of the integer input registers can be used by external RTDE clients (i.e URCAPS).'''
		return RtdeIntRegistersValue(self._instance.InputIntRegisters)

	@property
	def input_double_registers(self) -> RtdeDoubleRegistersValue:
		'''48 general purpose double registers. X: [0..23] - The lower range of the double input registers is reserved for FieldBus/PLC interface usage. X: [24..47] - The upper range of the double input registers can be used by external RTDE clients (i.e URCAPS).'''
		return RtdeDoubleRegistersValue(self._instance.InputDoubleRegisters)

	@property
	def external_force_torque(self) -> CartesianCoordinates:
		'''Input external wrench when using ft_rtde_input_enable builtin.'''
		return CartesianCoordinates(None, None, None, None, None, None, self._instance.ExternalForceTorque)

	@external_force_torque.setter
	def external_force_torque(self, value: CartesianCoordinates):
		self._instance.ExternalForceTorque = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeInputValues):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
