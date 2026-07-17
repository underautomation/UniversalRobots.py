from enum import IntEnum

class RobotModes(IntEnum):
	'''Robot running modes'''
	Other = -1 # Robot is in an obsolete CB2 mode
	Disconnected = 0 # Robot is not connected to its controller
	ConfirmSafety = 1 # Robot has stopped due to a Safety Stop
	Booting = 2 # The robot controller is booting
	PowerOff = 3 # The robot is powered off
	PowerOn = 4 # The robot is powered on
	Idle = 5 # Power is on but breaks are not released
	BackDrive = 6 # The robot is hand guided by pushing teached button
	Running = 7 # Robot is in normal mode
	UpdatingFirmware = 8 # Firmware is upgrading
