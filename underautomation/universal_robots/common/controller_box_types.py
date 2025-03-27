import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import ControllerBoxTypes as controller_box_types

class ControllerBoxTypes(int):
	UR3 = controller_box_types.UR3
	UR5 = controller_box_types.UR5
	UR10 = controller_box_types.UR10
	UR16 = controller_box_types.UR16
	UR20 = controller_box_types.UR20
	UR30 = controller_box_types.UR30
