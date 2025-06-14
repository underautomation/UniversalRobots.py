import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import GlobalVariableTypes as global_variable_types

class GlobalVariableTypes(int):
	String = global_variable_types.String
	List = global_variable_types.List
	Pose = global_variable_types.Pose
	Bool = global_variable_types.Bool
	Int = global_variable_types.Int
	Float = global_variable_types.Float
	Matrix = global_variable_types.Matrix
