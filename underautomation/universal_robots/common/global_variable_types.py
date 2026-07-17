from enum import IntEnum

class GlobalVariableTypes(IntEnum):
	'''Possible types of a variable'''
	None_ = 0 # Variable value is null, the value has not been assigned yet
	String = 1 # Variable value is a System.String
	List = 2 # Variable value is an array : GlobalVariableValue[]
	Pose = 3 # Variable value is a UnderAutomation.UniversalRobots.Pose
	Bool = 4 # Variable value is bool
	Int = 5 # Variable value is int
	Float = 6 # Variable value is float
	Matrix = 7 # Variable value is a matrix
