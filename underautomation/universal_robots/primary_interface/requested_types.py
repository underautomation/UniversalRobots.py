from enum import IntEnum

class RequestedTypes(IntEnum):
	'''Types for popup assignment'''
	Boolean = 0 # Popup for boolean value assignment
	Integer = 1 # Popup for integer number value assignment
	Float = 2 # Popup for float number value assignment
	String = 3 # Popup for string value assignment
	Pose = 4 # Popup for pose value assignment
	JointVector = 5 # Popup for joint vector value assignment
	Waypoint = 6 # Unused
	Expression = 7 # Unused
	None_ = 8 # It's a simple popup message
