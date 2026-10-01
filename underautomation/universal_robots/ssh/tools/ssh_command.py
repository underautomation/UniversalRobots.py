from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Ssh.Tools import SshCommand as ssh_command

class SshCommand:
	'''Represents SSH command that can be executed.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ssh_command()
		else:
			self._instance = _internal

	@typing.overload
	def execute(self, commandText: str) -> str: ...

	@typing.overload
	def execute(self) -> str: ...

	def execute(self, *args, **kwargs) -> str:
		'''Executes the specified command text.
		Executes command specified by command_text property.

		Arguments: (commandText)
		Arguments: ()
		:param commandText: The command text.
		:returns: Command execution result
		'''
		__a = _bind_overload(args, kwargs, ['commandText'], {})
		if __a is not None:
			commandText, = __a
			return self._instance.Execute(commandText)
		__a = _bind_overload(args, kwargs, [], {})
		if __a is not None:
			return self._instance.Execute()
		raise TypeError("execute(): no overload takes these arguments")

	def cancel_async(self) -> None:
		'''Cancels command execution in asynchronous scenarios.'''
		self._instance.CancelAsync()

	def dispose(self) -> None:
		'''Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.'''
		self._instance.Dispose()

	@property
	def command_text(self) -> str:
		'''Gets the command text.'''
		return self._instance.CommandText

	@property
	def command_timeout(self) -> typing.Any:
		'''Gets or sets the command timeout.'''
		return self._instance.CommandTimeout

	@command_timeout.setter
	def command_timeout(self, value: typing.Any):
		self._instance.CommandTimeout = value

	@property
	def exit_status(self) -> int:
		'''Gets the command exit status.'''
		return self._instance.ExitStatus

	@property
	def output_stream(self) -> typing.Any:
		'''Gets the output stream.'''
		return self._instance.OutputStream

	@property
	def extended_output_stream(self) -> typing.Any:
		'''Gets the extended output stream.'''
		return self._instance.ExtendedOutputStream

	@property
	def result(self) -> str:
		'''Gets the command execution result.'''
		return self._instance.Result

	@property
	def error(self) -> str:
		'''Gets the command execution error.'''
		return self._instance.Error

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SshCommand):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self._instance.Dispose()
		return False

def _bind_overload(args, kwargs, names, defaults):
	if len(args) > len(names) or any(k not in names[len(args):] for k in kwargs):
		return None
	values = list(args)
	for name in names[len(args):]:
		if name in kwargs:
			values.append(kwargs[name])
		elif name in defaults:
			values.append(defaults[name])
		else:
			return None
	return values
