import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.InterpreterMode.Internal import InterpreterModeClientParametersBase as interpreter_mode_client_parameters_base

class InterpreterModeClientParametersBase:
	'''Base class for Interpreter Mode connection parameters.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = interpreter_mode_client_parameters_base()
		else:
			self._instance = _internal

	@property
	def port(self) -> int:
		'''Interpreter Mode client TCP port. Default : 30020'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, InterpreterModeClientParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default Interpreter Mode server TCP port
InterpreterModeClientParametersBase.DEFAULT_PORT = interpreter_mode_client_parameters_base.DEFAULT_PORT
