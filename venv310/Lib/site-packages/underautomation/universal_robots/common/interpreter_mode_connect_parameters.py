import typing
from underautomation.universal_robots.interpreter_mode.internal.interpreter_mode_client_parameters_base import InterpreterModeClientParametersBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import InterpreterModeConnectParameters as interpreter_mode_connect_parameters

class InterpreterModeConnectParameters(InterpreterModeClientParametersBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = interpreter_mode_connect_parameters()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value
