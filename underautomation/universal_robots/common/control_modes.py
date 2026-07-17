from enum import IntEnum

class ControlModes(IntEnum):
	'''Robot control modes'''
	Position = 0 # Robot is position controlled
	Teach = 1 # The robot is hand guided by pushing teached button
	Force = 2 # Robot is force controlled. (For example : URScript force_mode() function is called)
	Torque = 3 # Robot is torque controlled
