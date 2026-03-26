import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Rtde import RtdeValue as rtde_value

class RtdeValue:
	'''Abstract base class for a single RTDE variable value exchanged between the client and the robot.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_value()
		else:
			self._instance = _internal

	@property
	def value(self) -> typing.Any:
		'''Gets or sets the current value as an untyped object.'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
