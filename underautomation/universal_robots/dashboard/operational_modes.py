from enum import IntEnum

class OperationalModes(IntEnum):
	'''Enumerates all robot operational modes'''
	Manual = 0 # Loading and editing programs is allowed
	Automatic = 1 # Loading and editing programs and installations is not allowed, only playing programs
	None_ = 2 # The password has not been set.
