import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Kinematics import SingularityType as singularity_type

class SingularityType(int):
	Wrist = singularity_type.Wrist
	Elbow = singularity_type.Elbow
	Shoulder = singularity_type.Shoulder
