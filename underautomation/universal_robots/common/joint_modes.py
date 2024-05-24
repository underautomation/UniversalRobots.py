import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import JointModes as joint_modes

class JointModes(int):
	ShuttingDown = joint_modes.ShuttingDown
	PartDCalibration = joint_modes.PartDCalibration
	Backdrive = joint_modes.Backdrive
	PowerOff = joint_modes.PowerOff
	NotResponding = joint_modes.NotResponding
	MotorInitialisation = joint_modes.MotorInitialisation
	Booting = joint_modes.Booting
	PartDCalibrationError = joint_modes.PartDCalibrationError
	Bootloder = joint_modes.Bootloder
	Calibration = joint_modes.Calibration
	Fault = joint_modes.Fault
	Running = joint_modes.Running
	Idle = joint_modes.Idle
