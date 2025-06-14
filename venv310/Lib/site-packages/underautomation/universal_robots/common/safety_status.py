import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import SafetyStatus as safety_status

class SafetyStatus(int):
	Normal = safety_status.Normal
	Reduced = safety_status.Reduced
	ProtectiveStop = safety_status.ProtectiveStop
	Recovery = safety_status.Recovery
	SafeguardStop = safety_status.SafeguardStop
	SystemEmergencyStop = safety_status.SystemEmergencyStop
	RobotEmergencyStop = safety_status.RobotEmergencyStop
	Violation = safety_status.Violation
	Fault = safety_status.Fault
	AutomaticModeSafeguardStop = safety_status.AutomaticModeSafeguardStop
	SystemThreePositionEnablingStop = safety_status.SystemThreePositionEnablingStop
