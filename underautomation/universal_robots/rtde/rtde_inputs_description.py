import typing
from __future__ import annotation
from underautomation.universal_robots.rtde.rtde_input_data_description import RtdeInputDataDescription
from underautomation.universal_robots.rtde.rtde_input_data import RtdeInputData
from UnderAutomation.UniversalRobots.Rtde import RtdeInputsDescription as rtde_inputs_description
from UnderAutomation.UniversalRobots.Rtde import RtdeInputData as rtde_input_data

class RtdeInputsDescription:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_inputs_description()
		else:
			self._instance = _internal

	def get(self, data: RtdeInputData) -> RtdeInputDataDescription:
		return RtdeInputDataDescription(self._instance.Get(rtde_input_data(int(data))))

	@property
	def items(self) -> typing.Any:
		return self._instance.Items

	@property
	def speed_slider_mask(self) -> RtdeInputDataDescription:
		'''0 = don't change speed slider with this input, 1 = use speed_slider_fraction to set speed slider value'''
		return RtdeInputDataDescription(self._instance.SpeedSliderMask)

	@property
	def speed_slider_fraction(self) -> RtdeInputDataDescription:
		'''new speed slider value'''
		return RtdeInputDataDescription(self._instance.SpeedSliderFraction)

	@property
	def standard_digital_output_mask(self) -> RtdeInputDataDescription:
		'''Standard digital output bit mask'''
		return RtdeInputDataDescription(self._instance.StandardDigitalOutputMask)

	@property
	def configurable_digital_output_mask(self) -> RtdeInputDataDescription:
		'''Configurable digital output bit mask'''
		return RtdeInputDataDescription(self._instance.ConfigurableDigitalOutputMask)

	@property
	def standard_digital_output(self) -> RtdeInputDataDescription:
		'''Standard digital outputs'''
		return RtdeInputDataDescription(self._instance.StandardDigitalOutput)

	@property
	def configurable_digital_output(self) -> RtdeInputDataDescription:
		'''Configurable digital outputs'''
		return RtdeInputDataDescription(self._instance.ConfigurableDigitalOutput)

	@property
	def standard_analog_output_mask(self) -> RtdeInputDataDescription:
		'''Standard analog output mask'''
		return RtdeInputDataDescription(self._instance.StandardAnalogOutputMask)

	@property
	def standard_analog_output_type(self) -> RtdeInputDataDescription:
		'''Output domain {0=current[mA], 1=voltage[V]}. Bits 0-1: standard_analog_output_0 | standard_analog_output_1'''
		return RtdeInputDataDescription(self._instance.StandardAnalogOutputType)

	@property
	def standard_analog_output0(self) -> RtdeInputDataDescription:
		'''Standard analog output 0 (ratio) [0..1]'''
		return RtdeInputDataDescription(self._instance.StandardAnalogOutput0)

	@property
	def standard_analog_output1(self) -> RtdeInputDataDescription:
		'''Standard analog output 1 (ratio) [0..1]'''
		return RtdeInputDataDescription(self._instance.StandardAnalogOutput1)

	@property
	def input_bt_registers0_to31(self) -> RtdeInputDataDescription:
		'''General purpose bits. This range of the boolean input registers is reserved for FieldBus/PLC interface usage.'''
		return RtdeInputDataDescription(self._instance.InputBtRegisters0To31)

	@property
	def input_bt_registers32_to63(self) -> RtdeInputDataDescription:
		'''General purpose bits. This range of the boolean input registers is reserved for FieldBus/PLC interface usage.'''
		return RtdeInputDataDescription(self._instance.InputBtRegisters32To63)

	@property
	def input_bit_registers(self) -> RtdeInputDataDescription:
		'''64 general purpose bits. X: [64..127] - The upper range of the boolean input registers can be used by external RTDE clients (i.e URCAPS).'''
		return RtdeInputDataDescription(self._instance.InputBitRegisters)

	@property
	def input_int_registers(self) -> RtdeInputDataDescription:
		'''48 general purpose integer registers. X: [0..23] - The lower range of the integer input registers is reserved for FieldBus/PLC interface usage. X: [24..47] - The upper range of the integer input registers can be used by external RTDE clients (i.e URCAPS).'''
		return RtdeInputDataDescription(self._instance.InputIntRegisters)

	@property
	def input_double_registers(self) -> RtdeInputDataDescription:
		'''48 general purpose double registers. X: [0..23] - The lower range of the double input registers is reserved for FieldBus/PLC interface usage. X: [24..47] - The upper range of the double input registers can be used by external RTDE clients (i.e URCAPS).'''
		return RtdeInputDataDescription(self._instance.InputDoubleRegisters)

	@property
	def external_force_torque(self) -> RtdeInputDataDescription:
		'''Input external wrench when using ft_rtde_input_enable builtin.'''
		return RtdeInputDataDescription(self._instance.ExternalForceTorque)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeInputsDescription):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
