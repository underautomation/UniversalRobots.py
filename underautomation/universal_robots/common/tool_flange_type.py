from enum import IntEnum

class ToolFlangeType(IntEnum):
	'''Version of the tool flange of a UR robot.'''
	Unknown = 0 # The tool flange version is not known.
	V1 = 1 # Tool flange version 1.
	V2 = 2 # Tool flange version 2 (tool voltage on connector T2, PolyScope X 10.15 and later).
