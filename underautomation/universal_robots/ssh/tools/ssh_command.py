import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Ssh.Tools import SshCommand as ssh_command

class SshCommand:
	'''Represents SSH command that can be executed.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ssh_command()
		else:
			self._instance = _internal

	def begin_execute(self, commandText: str, callback: typing.Any, state: typing.Any) -> typing.Any:
		'''Begins an asynchronous command execution.

		:param commandText: The command text.
		:param callback: An optional asynchronous callback, to be called when the command execution is complete.
		:param state: A user-provided object that distinguishes this particular asynchronous read request from other requests.
		:returns: An IAsyncResult that represents the asynchronous command execution, which could still be pending.
		'''
		return self._instance.BeginExecute(commandText, callback, state)

	def end_execute(self, asyncResult: typing.Any) -> str:
		'''Waits for the pending asynchronous command execution to complete.

		:param asyncResult: The reference to the pending asynchronous request to finish.
		:returns: Command execution result.
		'''
		return self._instance.EndExecute(asyncResult)

	def execute(self, commandText: str) -> str:
		'''Executes the specified command text.

		:param commandText: The command text.
		:returns: Command execution result
		'''
		return self._instance.Execute(commandText)

	def cancel_async(self) -> None:
		'''Cancels command execution in asynchronous scenarios.'''
		self._instance.CancelAsync()

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
