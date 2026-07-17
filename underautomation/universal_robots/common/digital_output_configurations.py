from enum import IntEnum

class DigitalOutputConfigurations(IntEnum):
	'''Digital output configuration (NPN, PNP, Push/Pull)'''
	SinkingNPN = 1 # Sinking (NOPN)
	SourcingPNP = 2 # Sourcing (PNP)
	PushPull = 3 # Push / Pull
