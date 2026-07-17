from enum import IntEnum

class RobotModelsExtended(IntEnum):
	'''Model of a UR robot (including e-Series and extended payload models)'''
	UR3e = 0 # UR3e (e-Series).
	UR5e = 1 # UR5e (e-Series).
	UR7e = 2 # UR7e (e-Series).
	UR10e = 3 # UR10e (e-Series).
	UR12e = 4 # UR12e (e-Series).
	UR16e = 5 # UR16e (e-Series).
	UR15 = 6 # UR15 robot model.
	UR18 = 7 # UR18 robot model.
	UR20 = 8 # UR20 robot model.
	UR30 = 9 # UR30 robot model.
	UR8Long = 10 # UR8 Long robot model.
	UR3 = 11 # UR3 (CB-Series).
	UR5 = 12 # UR5 (CB-Series).
	UR10 = 13 # UR10 (CB-Series).
