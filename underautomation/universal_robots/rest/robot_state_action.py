import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rest import RobotStateAction as robot_state_action

class RobotStateAction(int):
	UNLOCK_PROTECTIVE_STOP = robot_state_action.UNLOCK_PROTECTIVE_STOP
	RESTART_SAFETY = robot_state_action.RESTART_SAFETY
	POWER_OFF = robot_state_action.POWER_OFF
	POWER_ON = robot_state_action.POWER_ON
	BRAKE_RELEASE = robot_state_action.BRAKE_RELEASE
