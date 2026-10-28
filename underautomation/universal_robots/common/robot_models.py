from enum import IntEnum

class RobotModels(IntEnum):
	'''Model of a UR robot'''
	UR5 = 1 # UR5 robot model.
	UR10 = 2 # UR10 robot model.
	UR3 = 3 # UR3 robot model.
	UR16 = 4 # UR16 robot model.
	UR20 = 7 # UR20 robot model.
	UR30 = 8 # UR30 robot model.
	UR8L = 6 # UR8 Long robot model.
	UR18 = 5 # UR18 robot model.
	UR15 = 9 # UR15 robot model.
	UR10G1750 = 12 # UR10 G 1750 robot model (G Series).
	UR17G1300 = 13 # UR17 G 1300 robot model (G Series).
	UR18G950 = 14 # UR18 G 950 robot model (G Series).
	Unknown = -128 # The model is not known. Returned by robot_model_from_value() for a value this SDK does not recognize.
