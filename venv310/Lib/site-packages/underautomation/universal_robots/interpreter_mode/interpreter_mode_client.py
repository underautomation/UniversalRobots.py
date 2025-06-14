import typing
from underautomation.universal_robots.interpreter_mode.internal.interpreter_mode_client_base import InterpreterModeClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.InterpreterMode import InterpreterModeClient as interpreter_mode_client

class InterpreterModeClient(InterpreterModeClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = interpreter_mode_client()
		else:
			self._instance = _internal
	def connect(self, ip: str, port: int=30020) -> None:
		self._instance.Connect(ip, port)
