from enum import IntEnum

class ToolModes(IntEnum):
	'''Tool modes'''
	Bootloader = 249 # Bootloader
	Running = 253 # Running
	Idle = 255 # Idle
