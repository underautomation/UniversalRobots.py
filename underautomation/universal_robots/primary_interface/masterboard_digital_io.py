from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.PrimaryInterface import MasterboardDigitalIO as masterboard_digital_io

class MasterboardDigitalIO:
	'''Represents the state of digital I/O pins on the UR controller masterboard, including standard digital, configurable, and tool digital pins.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = masterboard_digital_io()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def value(self) -> int:
		'''Register value'''
		return self._instance.Value

	@property
	def bit_array(self) -> typing.Any:
		'''Register value seen as a bool array'''
		return self._instance.BitArray

	@property
	def digital0(self) -> bool:
		'''State of standard digital I/O pin 0.'''
		return self._instance.Digital0

	@property
	def digital1(self) -> bool:
		'''State of standard digital I/O pin 1.'''
		return self._instance.Digital1

	@property
	def digital2(self) -> bool:
		'''State of standard digital I/O pin 2.'''
		return self._instance.Digital2

	@property
	def digital3(self) -> bool:
		'''State of standard digital I/O pin 3.'''
		return self._instance.Digital3

	@property
	def digital4(self) -> bool:
		'''State of standard digital I/O pin 4.'''
		return self._instance.Digital4

	@property
	def digital5(self) -> bool:
		'''State of standard digital I/O pin 5.'''
		return self._instance.Digital5

	@property
	def digital6(self) -> bool:
		'''State of standard digital I/O pin 6.'''
		return self._instance.Digital6

	@property
	def digital7(self) -> bool:
		'''State of standard digital I/O pin 7.'''
		return self._instance.Digital7

	@property
	def configurable0(self) -> bool:
		'''State of configurable digital I/O pin 0.'''
		return self._instance.Configurable0

	@property
	def configurable1(self) -> bool:
		'''State of configurable digital I/O pin 1.'''
		return self._instance.Configurable1

	@property
	def configurable2(self) -> bool:
		'''State of configurable digital I/O pin 2.'''
		return self._instance.Configurable2

	@property
	def configurable3(self) -> bool:
		'''State of configurable digital I/O pin 3.'''
		return self._instance.Configurable3

	@property
	def configurable4(self) -> bool:
		'''State of configurable digital I/O pin 4.'''
		return self._instance.Configurable4

	@property
	def configurable5(self) -> bool:
		'''State of configurable digital I/O pin 5.'''
		return self._instance.Configurable5

	@property
	def configurable6(self) -> bool:
		'''State of configurable digital I/O pin 6.'''
		return self._instance.Configurable6

	@property
	def configurable7(self) -> bool:
		'''State of configurable digital I/O pin 7.'''
		return self._instance.Configurable7

	@property
	def tool_digital0(self) -> bool:
		'''State of tool digital I/O pin 0.'''
		return self._instance.ToolDigital0

	@property
	def tool_digital1(self) -> bool:
		'''State of tool digital I/O pin 1.'''
		return self._instance.ToolDigital1

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MasterboardDigitalIO):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
