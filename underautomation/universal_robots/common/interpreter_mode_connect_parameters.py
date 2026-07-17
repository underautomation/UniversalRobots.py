from __future__ import annotations
import typing
from underautomation.universal_robots.interpreter_mode.internal.interpreter_mode_client_parameters_base import InterpreterModeClientParametersBase
from UnderAutomation.UniversalRobots.Common import InterpreterModeConnectParameters as interpreter_mode_connect_parameters

class InterpreterModeConnectParameters(InterpreterModeClientParametersBase):
	'''Setup Interpreter Mode Client'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = interpreter_mode_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Enable Interpreter Mode client communication Default value is false'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, InterpreterModeConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
