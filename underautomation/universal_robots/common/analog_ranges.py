from enum import IntEnum

class AnalogRanges(IntEnum):
	'''Analog units of analog inputs and outputs'''
	Current = 0 # The analog value is in Amps (A)
	Voltage = 1 # The analog value is in Volts (V)
