from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Internal import RtdeOverrunException as rtde_overrun_exception

class RtdeOverrunException:
	'''Exception thrown when RTDE data cannot be consumed fast enough, causing the input buffer to fill up. This typically occurs when the OutputDataReceived event handler takes longer to execute than the interval between RTDE messages.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RtdeOverrunException class with a default diagnostic message.'''
		if(_internal == 0):
			self._instance = rtde_overrun_exception()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeOverrunException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
