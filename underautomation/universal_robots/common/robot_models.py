import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import RobotModels as robot_models

class RobotModels(int):
	UR3 = robot_models.UR3
	UR5 = robot_models.UR5
	UR10 = robot_models.UR10
	UR16 = robot_models.UR16
