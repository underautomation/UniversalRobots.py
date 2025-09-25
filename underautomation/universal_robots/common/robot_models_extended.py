import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import RobotModelsExtended as robot_models_extended

class RobotModelsExtended(int):
	UR3e = robot_models_extended.UR3e
	UR5e = robot_models_extended.UR5e
	UR7e = robot_models_extended.UR7e
	UR10e = robot_models_extended.UR10e
	UR12e = robot_models_extended.UR12e
	UR16e = robot_models_extended.UR16e
	UR15 = robot_models_extended.UR15
	UR20 = robot_models_extended.UR20
	UR30 = robot_models_extended.UR30
	UR3 = robot_models_extended.UR3
	UR5 = robot_models_extended.UR5
	UR10 = robot_models_extended.UR10
