from enum import IntEnum

class PackageUnit(IntEnum):
	'''Physical units of receives measures'''
	NoUnit = 0 # No unit
	Radian = 1 # rad
	RadianPerSecond = 2 # rad/s
	RadianPerSecondSquared = 3 # rad/s²
	Meter = 4 # m
	MeterPerSecond = 5 # m/s
	MetersPerSecondSquared = 6 # m/s²
	CelsiusDegree = 7 # °C
	Volt = 8 # V
	Amp = 9 # A
