import typing
from underautomation.universal_robots.interpreter_mode.command_response_status import CommandResponseStatus
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.InterpreterMode import CommandResponse as command_response

class CommandResponse:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = command_response()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def status(self) -> CommandResponseStatus:
		return CommandResponseStatus(self._instance.Status)
	@property
	def id(self) -> int:
		return self._instance.Id
	@property
	def body(self) -> str:
		return self._instance.Body
	@property
	def raw_answer(self) -> str:
		return self._instance.RawAnswer
	@property
	def command(self) -> str:
		return self._instance.Command
