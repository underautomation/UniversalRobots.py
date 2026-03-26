from enum import IntEnum

class LicenseState(IntEnum):
	'''States that can take a license'''
	None_ = -1 # No license has been provided
	Invalid = 0 # The pair License Identifier and License Key are incompatible, you cannot use the library
	Trial = 1 # The library is in a trial period, you can use the library
	ExtraTrial = 2 # The library is in an extra trial period, you can use the library
	Expired = 3 # The trial period as expired, you no more can use the library
	MaintenanceNeeded = 4 # Your license does not allow you to use such a recent release. Please buy maintenance to use this version
	Licensed = 5 # Congratulations, the library is licensed.
