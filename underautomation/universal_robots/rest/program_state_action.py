from enum import IntEnum

class ProgramStateAction(IntEnum):
	'''Actions available for changing the program state via REST API'''
	play = 0 # Start or resume playing the program
	pause = 1 # Pause the running program
	stop = 2 # Stop the running program
	resume = 3 # Resume a paused program
