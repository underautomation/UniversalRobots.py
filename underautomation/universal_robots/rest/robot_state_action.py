from enum import IntEnum

class RobotStateAction(IntEnum):
	'''Actions available for changing the robot's operational state via REST API'''
	UNLOCK_PROTECTIVE_STOP = 0 # Unlocks the robot from a protective stop state
	RESTART_SAFETY = 1 # Restarts the safety system
	POWER_OFF = 2 # Powers off the robot
	POWER_ON = 3 # Powers on the robot
	BRAKE_RELEASE = 4 # Releases the robot brakes
