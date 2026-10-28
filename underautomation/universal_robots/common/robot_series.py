from enum import IntEnum

class RobotSeries(IntEnum):
	'''Series of a UR robot.'''
	Unknown = -128 # The series is not known. Returned for a value this SDK does not recognize.
	CB3 = 1 # CB3 series (UR3, UR5, UR10).
	ESeries = 2 # e-Series (UR3e, UR5e, UR10e, UR16e...).
	URSeries = 3 # UR Series (UR15, UR18, UR20, UR30, UR8 Long).
	GSeries = 4 # G Series (UR10 G 1750, UR17 G 1300, UR18 G 950).
