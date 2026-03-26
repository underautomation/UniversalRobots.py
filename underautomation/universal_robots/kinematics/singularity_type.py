from enum import IntEnum

class SingularityType(IntEnum):
	'''Types of singularities'''
	None_ = 0 # No singularity
	Wrist = 1 # Wrist singularity
	Elbow = 2 # Elbow singularity
	Shoulder = 4 # Shoulder singularity
