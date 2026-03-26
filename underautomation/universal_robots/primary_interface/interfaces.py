from enum import IntEnum

class Interfaces(IntEnum):
	'''TCP ports to communicate with an UR controller'''
	PrimaryInterface = 30001 # The default port that allow reading data and sending URScript
	SecondaryInterface = 30002 # The secondary port with same features as PrimaryClient
	PrimaryInterfaceReadOnly = 30011 # This port can only read data. It is unable to send URScript.
	SecondaryInterfaceReadOnly = 30012 # A secondary port that can only read data. It is unable to send URScript.
