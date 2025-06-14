import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import AnalogRanges as analog_ranges

class AnalogRanges(int):
	Current = analog_ranges.Current
	Voltage = analog_ranges.Voltage
