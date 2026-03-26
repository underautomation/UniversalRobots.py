from enum import IntEnum

class RtdeInputData(IntEnum):
	SpeedSliderMask = 0 # 0 = don't change speed slider with this input, 1 = use speed_slider_fraction to set speed slider value
	SpeedSliderFraction = 1 # new speed slider value
	StandardDigitalOutputMask = 2 # Standard digital output bit mask
	ConfigurableDigitalOutputMask = 3 # Configurable digital output bit mask
	StandardDigitalOutput = 4 # Standard digital outputs
	ConfigurableDigitalOutput = 5 # Configurable digital outputs
	StandardAnalogOutputMask = 6 # Standard analog output mask
	StandardAnalogOutputType = 7 # Output domain {0=current[mA], 1=voltage[V]}. Bits 0-1: standard_analog_output_0 | standard_analog_output_1
	StandardAnalogOutput0 = 8 # Standard analog output 0 (ratio) [0..1]
	StandardAnalogOutput1 = 9 # Standard analog output 1 (ratio) [0..1]
	InputBtRegisters0To31 = 10 # General purpose bits. This range of the boolean input registers is reserved for FieldBus/PLC interface usage.
	InputBtRegisters32To63 = 11 # General purpose bits. This range of the boolean input registers is reserved for FieldBus/PLC interface usage.
	InputBitRegisters = 12 # 64 general purpose bits. X: [64..127] - The upper range of the boolean input registers can be used by external RTDE clients (i.e URCAPS).
	InputIntRegisters = 13 # 48 general purpose integer registers. X: [0..23] - The lower range of the integer input registers is reserved for FieldBus/PLC interface usage. X: [24..47] - The upper range of the integer input registers can be used by external RTDE clients (i.e URCAPS).
	InputDoubleRegisters = 14 # 48 general purpose double registers. X: [0..23] - The lower range of the double input registers is reserved for FieldBus/PLC interface usage. X: [24..47] - The upper range of the double input registers can be used by external RTDE clients (i.e URCAPS).
	ExternalForceTorque = 15 # Input external wrench when using ft_rtde_input_enable builtin.
