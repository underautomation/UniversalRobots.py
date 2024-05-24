import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import OutputModes as output_modes

class OutputModes(int):
	StandardOutput = output_modes.StandardOutput
	DualPinPower = output_modes.DualPinPower
