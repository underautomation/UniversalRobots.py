from enum import IntEnum

class JointModes(IntEnum):
	'''Joint modes'''
	ShuttingDown = 236 # Joint is shutting down.
	PartDCalibration = 237 # Joint is in part D calibration mode.
	Backdrive = 238 # Joint is in backdrive mode.
	PowerOff = 239 # Joint is powered off.
	NotResponding = 245 # Joint is not responding.
	MotorInitialisation = 246 # Joint motor is initializing.
	Booting = 247 # Joint is booting.
	PartDCalibrationError = 248 # Joint part D calibration encountered an error.
	Bootloader = 249 # Joint is in bootloader mode.
	Calibration = 250 # Joint is calibrating.
	Fault = 252 # Joint is in a fault state.
	Running = 253 # Joint is running normally.
	Idle = 255 # Joint is idle.
