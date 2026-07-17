from enum import IntEnum

class SafetyStatus(IntEnum):
	'''Safety modes'''
	Normal = 1 # Safety is in normal operating conditions
	Reduced = 2 # Speed is reduced
	ProtectiveStop = 3 # Protective safeguard Stop. This safety function is triggeredby an external protective device using safety inputs which will trigger a Cat 2 stop3per IEC 60204-1.
	Recovery = 4 # When a safety limit is violated, the safety system must be restarted.
	SafeguardStop = 5 # (SI0 + SI1 + SBUS) Physical s-stop interface input
	SystemEmergencyStop = 6 # (EA + EB + SBUS->Euromap67) Physical e-stop interface input activated
	RobotEmergencyStop = 7 # (EA + EB + SBUS->Screen) Physical e-stop interface input activated
	Violation = 8 # Safety is in violation mode (for example, violation of the allowed delay between redundant signals)
	Fault = 9 # Safety is in fault mode
	AutomaticModeSafeguardStop = 10 # Automatic mode safeguard stop is active.
	SystemThreePositionEnablingStop = 11 # System three-position enabling device stop is active.
