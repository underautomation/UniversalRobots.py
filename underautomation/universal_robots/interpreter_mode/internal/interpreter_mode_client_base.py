import typing
from underautomation.universal_robots.interpreter_mode.command_response import CommandResponse
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.InterpreterMode.Internal import InterpreterModeClientBase as interpreter_mode_client_base

class InterpreterModeClientBase(URServiceBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = interpreter_mode_client_base()
		else:
			self._instance = _internal
	def execute_command(self, command: str) -> CommandResponse:
		return CommandResponse(self._instance.ExecuteCommand(command))
	def end_interpreter(self) -> CommandResponse:
		return CommandResponse(self._instance.EndInterpreter())
	def clear_interpreter(self) -> CommandResponse:
		return CommandResponse(self._instance.ClearInterpreter())
	def abort(self) -> CommandResponse:
		return CommandResponse(self._instance.Abort())
	def skip_buffer(self) -> CommandResponse:
		return CommandResponse(self._instance.SkipBuffer())
	def state_last_executed(self) -> CommandResponse:
		return CommandResponse(self._instance.StateLastExecuted())
	def state_last_interpreted(self) -> CommandResponse:
		return CommandResponse(self._instance.StateLastInterpreted())
	def state_last_cleared(self) -> CommandResponse:
		return CommandResponse(self._instance.StateLastCleared())
	def state_last_unexecuted(self) -> CommandResponse:
		return CommandResponse(self._instance.StateLastUnexecuted())
	def disconnect(self) -> None:
		self._instance.Disconnect()
	@property
	def ip(self) -> str:
		return self._instance.IP
	@property
	def port(self) -> int:
		return self._instance.Port
	@port.setter
	def port(self, value: int):
		self._instance.Port = value
	@property
	def connected(self) -> bool:
		return self._instance.Connected
