from enum import IntEnum

class RTDEStates(IntEnum):
	'''Represents the current state of the RTDE connection lifecycle.'''
	Disabled = 0 # RTDE is not connected.
	Connecting = 1 # RTDE connection and recipe setup are in progress.
	Started = 2 # RTDE is actively streaming data.
	Paused = 3 # RTDE streaming is paused but the connection remains open.
