import typing
from __future__ import annotation
from underautomation.universal_robots.interpreter_mode.command_response import CommandResponse
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from UnderAutomation.UniversalRobots.InterpreterMode.Internal import InterpreterModeClientBase as interpreter_mode_client_base

class InterpreterModeClientBase(URServiceBase):
	'''Base class for the Interpreter Mode client, providing TCP communication and built-in interpreter commands.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = interpreter_mode_client_base()
		else:
			self._instance = _internal

	def execute_command(self, command: str) -> CommandResponse:
		'''Executes a command on the Interpreter Mode

		:param command: URScript statement to execute
		'''
		return CommandResponse(self._instance.ExecuteCommand(command))

	def end_interpreter(self) -> CommandResponse:
		'''Ends the interpreter mode, and causes the interpreter_mode() function to return. This function can be compiled into the program by sending it to the interpreter socket(30020) as any other statement, or can be called from anywhere else in the program. By default everything interpreted will be cleared when ending, though the state of the robot, the modifications to local variables from the enclosing scope, and the global variables will remain affected by any changes made.The interpreter thread will be idle after this call.'''
		return CommandResponse(self._instance.EndInterpreter())

	def clear_interpreter(self) -> CommandResponse:
		'''Clears all interpreted statements, objects, functions, threads, etc. generated in the current interpreter mode.Threads started in current interpreter session will be stopped, and deleted. Variables defined outside of the current interpreter mode will not be affected by a call to thisfunction. Only statements interpreted before the clear_interpreter() function will be cleared. Statements sent after clear_interpreter() will be queued. When cleaning is done, any statements queued are interpreted and responded to. Note that commands such as abort, skipbuffer and state commands are executed as soon as they are received.'''
		return CommandResponse(self._instance.ClearInterpreter())

	def abort(self) -> CommandResponse:
		'''The interpreter mode offers a mechanism to abort limited number of script functions, even if they are called from the main program. Currently only movej and movel can be aborted. Aborting a movement will result in a controlled stop if no blend radius is defined. If a blend radius is defined then a blend with the next movement will be initiated right away if not already in an initial blend, otherwise the command is ignored. Return value should be ignored'''
		return CommandResponse(self._instance.Abort())

	def skip_buffer(self) -> CommandResponse:
		'''The interpreter mode furthermore supports the opportunity to skip already sent but not executed statements.The interpreter thread will then(after finishing the currently executing statement) skip all received but not executed statements. After the skip, the interpreter thread will idle until new statements are received.skipbuffer will only skip already received statements, new statements can therefore be send right away. Return value should be ignored'''
		return CommandResponse(self._instance.SkipBuffer())

	def state_last_executed(self) -> CommandResponse:
		'''Replies with the largest id of a statement that has started being executed.'''
		return CommandResponse(self._instance.StateLastExecuted())

	def state_last_interpreted(self) -> CommandResponse:
		'''Replies with the latest interpreted id, i.e. the highest number of interpreted statement so far.'''
		return CommandResponse(self._instance.StateLastInterpreted())

	def state_last_cleared(self) -> CommandResponse:
		'''Replies with the id for the latest statement to be cleared from the interpreter mode. This clear can happen when ending interpreter mode, or by calls to clear_interpreter()'''
		return CommandResponse(self._instance.StateLastCleared())

	def state_last_unexecuted(self) -> CommandResponse:
		'''Replies with the number of non executed statements, i.e. the number of statements that would have be skipped if skipbuffer was called instead.'''
		return CommandResponse(self._instance.StateLastUnexecuted())

	def disconnect(self) -> None:
		'''Disconnect interpreter mode socket connection'''
		self._instance.Disconnect()

	@property
	def ip(self) -> str:
		'''IP of the robot to connect to for sending commands'''
		return self._instance.IP

	@property
	def port(self) -> int:
		'''Interpreter mode server port'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	@property
	def connected(self) -> bool:
		'''Indicates that the interpreter mode client is connected and ready to send commands'''
		return self._instance.Connected

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, InterpreterModeClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
