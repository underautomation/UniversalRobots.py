from enum import IntEnum

class UserRoles(IntEnum):
	'''Enumerates all user roles'''
	Programmer = 0 # In Setup Robot, buttons "Update", "Set Password", "Network", "Time" and "URCaps" are disabled, "Expert Mode" is available (if correct password is supplied)
	Operator = 1 # Only "RUN Program" And "SHUTDOWN Robot" buttons are enabled, "Expert Mode" cannot be activated
	None_ = 2 # All buttons enabled, "Expert Mode" is available (if correct password is supplied)
	Locked = 3 # All buttons disabled and "Expert Mode" cannot be activated
	restricted = 4 # Works like "operator" but does not give access to the move tab. (From FW 3.1.17136)
