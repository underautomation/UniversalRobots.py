from enum import IntEnum

class CommandResponseStatus(IntEnum):
	'''Type of response of an Interpreter Mode command'''
	Error = -1 # Something went wrong when receiving response
	Ack = 0 # The command compilation succeed and Interpreter mode will execute the statement
	Discard = 1 # Program is not running or the statement results in a compilation or linker error
	State = 2 # Answer from a state command
