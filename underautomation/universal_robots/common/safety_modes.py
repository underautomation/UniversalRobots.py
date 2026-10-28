from enum import IntEnum

class SafetyModes(IntEnum):
	'''Safety modes of a UR robot.'''
	Unknown = -128 # The safety mode is not known. Returned for a value this SDK does not recognize.
	Normal = 1 # Normal operation.
	Reduced = 2 # Reduced mode: speed and force limits are lower.
	ProtectiveStop = 3 # Protective stop.
	Recovery = 4 # Recovery mode after a safety limit violation.
	SafeguardStop = 5 # Safeguard stop.
	SystemEmergencyStop = 6 # System emergency stop.
	RobotEmergencyStop = 7 # Robot emergency stop.
	Violation = 8 # Safety violation.
	Fault = 9 # Safety fault.
	ValidateJointId = 10 # The safety system validates the joint identification.
	UndefinedSafetyMode = 11 # Undefined safety mode.
	AutomaticModeSafeguardStop = 12 # Safeguard stop in automatic mode.
	SystemThreePositionEnablingStop = 13 # System three-position enabling device stop.
	TpThreePositionEnablingStop = 14 # Teach pendant three-position enabling device stop.
	ImmiEmergencyStop = 15 # Emergency stop from the IMMI interface.
	ImmiSafeguardStop = 16 # Safeguard stop from the IMMI interface.
	ProfisafeWaitingForParameters = 17 # PROFIsafe is waiting for its parameters.
	ProfisafeAutomaticModeSafeguardStop = 18 # PROFIsafe safeguard stop in automatic mode.
	ProfisafeSafeguardStop = 19 # PROFIsafe safeguard stop.
	ProfisafeEmergencyStop = 20 # PROFIsafe emergency stop.
	SafetyApiSafeguardStop = 22 # Safeguard stop requested through the safety API.
