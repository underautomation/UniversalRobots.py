from enum import IntEnum

class GlobalVariablesFirmwareVersion(IntEnum):
	'''Firmware version for variable decoding'''
	UpTo32 = 0 # FW up to 3.2
	UpTo59 = 1 # FW up to 5.9
	Latest = 2 # Recent firmware
