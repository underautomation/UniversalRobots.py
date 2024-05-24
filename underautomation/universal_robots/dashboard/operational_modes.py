import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Dashboard import OperationalModes as operational_modes

class OperationalModes(int):
	Manual = operational_modes.Manual
	Automatic = operational_modes.Automatic
