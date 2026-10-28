from enum import IntEnum

class ControlBoxType(IntEnum):
	'''Type of the control box of a UR robot.'''
	Unknown = 0 # The control box type is not known.
	CB5 = 5 # CB5 control box.
	CB7 = 7 # CB7 control box. It has no standard digital outputs.
