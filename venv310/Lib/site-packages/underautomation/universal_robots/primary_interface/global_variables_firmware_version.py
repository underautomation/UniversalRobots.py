import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.PrimaryInterface import GlobalVariablesFirmwareVersion as global_variables_firmware_version

class GlobalVariablesFirmwareVersion(int):
	UpTo32 = global_variables_firmware_version.UpTo32
	UpTo59 = global_variables_firmware_version.UpTo59
	Latest = global_variables_firmware_version.Latest
