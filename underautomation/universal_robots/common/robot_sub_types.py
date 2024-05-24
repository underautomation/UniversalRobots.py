import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import RobotSubTypes as robot_sub_types

class RobotSubTypes(int):
	CB2Serie = robot_sub_types.CB2Serie
	CB3Serie = robot_sub_types.CB3Serie
	ESerie = robot_sub_types.ESerie
