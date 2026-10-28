from enum import IntEnum

class FlightReportTypes(IntEnum):
	'''Types of flight report that the robot can generate.'''
	Controller = 0 # Report of the controller.
	Software = 1 # Report of the software.
	System = 2 # Report of the system.
