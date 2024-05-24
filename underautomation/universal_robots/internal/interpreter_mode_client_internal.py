import typing
from underautomation.universal_robots.interpreter_mode.internal.interpreter_mode_client_base import InterpreterModeClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Internal import InterpreterModeClientInternal as interpreter_mode_client_internal

class InterpreterModeClientInternal(InterpreterModeClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = interpreter_mode_client_internal()
		else:
			self._instance = _internal
	def connect(self, port: int=30020) -> None:
		self._instance.Connect(port)
