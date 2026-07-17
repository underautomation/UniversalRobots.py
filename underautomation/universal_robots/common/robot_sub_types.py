from enum import IntEnum

class RobotSubTypes(IntEnum):
	'''Robot sub type (e-Serie or CB-Serie)'''
	CB2Serie = 1 # CB2-series (Firmware 1.x)
	CB3Serie = 2 # CB3-series (Firmware 3.x)
	ESerie = 3 # e-series (Firmware 5.x)
