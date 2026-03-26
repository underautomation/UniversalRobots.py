from enum import IntEnum

class RestProgramState(IntEnum):
	'''Program state values returned by the REST API'''
	Unknown = 0 # Unknown state
	Stopped = 1 # Program is stopped
	Playing = 2 # Program is playing
	Paused = 3 # Program is paused
