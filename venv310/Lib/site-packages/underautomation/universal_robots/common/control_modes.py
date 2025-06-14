import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import ControlModes as control_modes

class ControlModes(int):
	Position = control_modes.Position
	Teach = control_modes.Teach
	Force = control_modes.Force
	Torque = control_modes.Torque
