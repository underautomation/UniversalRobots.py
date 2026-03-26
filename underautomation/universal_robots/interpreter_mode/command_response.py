import typing
from __future__ import annotation
from underautomation.universal_robots.interpreter_mode.command_response_status import CommandResponseStatus
from UnderAutomation.UniversalRobots.InterpreterMode import CommandResponse as command_response
from UnderAutomation.UniversalRobots.InterpreterMode import CommandResponseStatus as command_response_status

class CommandResponse:
	'''Response to an Interpreter Mode command'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = command_response()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def status(self) -> CommandResponseStatus:
		'''Response type to check if command succeed'''
		return CommandResponseStatus(int(self._instance.Status))

	@property
	def id(self) -> int:
		'''Command unique identifier'''
		return self._instance.Id

	@property
	def body(self) -> str:
		'''Answer from the interpreter mode'''
		return self._instance.Body

	@property
	def raw_answer(self) -> str:
		'''Raw line sent from the controller'''
		return self._instance.RawAnswer

	@property
	def command(self) -> str:
		'''Command sent to the interpreter mode'''
		return self._instance.Command

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CommandResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
