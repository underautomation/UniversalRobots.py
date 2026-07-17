from enum import IntEnum

class ProgramStates(IntEnum):
	'''Enumerate possible states of a program.'''
	Stopped = 0 # No program is running.
	Playing = 1 # Program is running.
	Paused = 2 # Program is paused.
