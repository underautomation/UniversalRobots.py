import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import RobotModes as robot_modes

class RobotModes(int):
	Other = robot_modes.Other
	Disconnected = robot_modes.Disconnected
	ConfirmSafety = robot_modes.ConfirmSafety
	Booting = robot_modes.Booting
	PowerOff = robot_modes.PowerOff
	PowerOn = robot_modes.PowerOn
	Idle = robot_modes.Idle
	BackDrive = robot_modes.BackDrive
	Running = robot_modes.Running
	UpdatingFirmware = robot_modes.UpdatingFirmware
