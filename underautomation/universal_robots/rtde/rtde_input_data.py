import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rtde import RtdeInputData as rtde_input_data

class RtdeInputData(int):
	SpeedSliderMask = rtde_input_data.SpeedSliderMask
	SpeedSliderFraction = rtde_input_data.SpeedSliderFraction
	StandardDigitalOutputMask = rtde_input_data.StandardDigitalOutputMask
	ConfigurableDigitalOutputMask = rtde_input_data.ConfigurableDigitalOutputMask
	StandardDigitalOutput = rtde_input_data.StandardDigitalOutput
	ConfigurableDigitalOutput = rtde_input_data.ConfigurableDigitalOutput
	StandardAnalogOutputMask = rtde_input_data.StandardAnalogOutputMask
	StandardAnalogOutputType = rtde_input_data.StandardAnalogOutputType
	StandardAnalogOutput0 = rtde_input_data.StandardAnalogOutput0
	StandardAnalogOutput1 = rtde_input_data.StandardAnalogOutput1
	InputBtRegisters0To31 = rtde_input_data.InputBtRegisters0To31
	InputBtRegisters32To63 = rtde_input_data.InputBtRegisters32To63
	InputBitRegisters = rtde_input_data.InputBitRegisters
	InputIntRegisters = rtde_input_data.InputIntRegisters
	InputDoubleRegisters = rtde_input_data.InputDoubleRegisters
	ExternalForceTorque = rtde_input_data.ExternalForceTorque
