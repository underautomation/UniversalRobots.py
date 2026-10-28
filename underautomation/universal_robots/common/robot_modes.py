from enum import IntEnum

class RobotModes(IntEnum):
	'''Robot running modes'''
	Other = -1 # The robot has no controller (value -1), or it is in an obsolete CB2 mode
	Unknown = -128 # The mode is not known. Returned by robot_mode_from_value() for a value this SDK does not recognize.
	Disconnected = 0 # Robot is not connected to its controller
	ConfirmSafety = 1 # Robot has stopped due to a Safety Stop
	Booting = 2 # The robot controller is booting
	PowerOff = 3 # The robot is powered off
	PowerOn = 4 # The robot is powered on
	Idle = 5 # Power is on but breaks are not released
	BackDrive = 6 # The robot is hand guided by pushing teached button
	Running = 7 # Robot is in normal mode
	UpdatingFirmware = 8 # Firmware is upgrading
