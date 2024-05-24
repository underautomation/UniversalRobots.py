import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import ToolModes as tool_modes

class ToolModes(int):
	Bootloader = tool_modes.Bootloader
	Running = tool_modes.Running
	Idle = tool_modes.Idle
