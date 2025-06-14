import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.PrimaryInterface import RequestedTypes as requested_types

class RequestedTypes(int):
	Boolean = requested_types.Boolean
	Integer = requested_types.Integer
	Float = requested_types.Float
	String = requested_types.String
	Pose = requested_types.Pose
	JointVector = requested_types.JointVector
	Waypoint = requested_types.Waypoint
	Expression = requested_types.Expression
