from __future__ import annotations
import typing
from underautomation.universal_robots.interpreter_mode.internal.interpreter_mode_client_base import InterpreterModeClientBase
from UnderAutomation.UniversalRobots.Internal import InterpreterModeClientInternal as interpreter_mode_client_internal

class InterpreterModeClientInternal(InterpreterModeClientBase):
	'''Internal implementation of the Interpreter Mode client that delegates connection to the parent UR instance.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = interpreter_mode_client_internal()
		else:
			self._instance = _internal

	def connect(self, port: int=30020) -> None:
		'''Enable Interpreter Mode client connection'''
		self._instance.Connect(port)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, InterpreterModeClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
