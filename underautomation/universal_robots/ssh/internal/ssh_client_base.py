from __future__ import annotations
import typing
from underautomation.universal_robots.ssh.tools.ssh_command import SshCommand
from underautomation.universal_robots.ssh.tools.shell import Shell
from underautomation.universal_robots.ssh.tools.shell_stream import ShellStream
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from underautomation.universal_robots.ssh.tools.common.terminal_modes import TerminalModes
from UnderAutomation.UniversalRobots.Ssh.Internal import SshClientBase as ssh_client_base
from UnderAutomation.UniversalRobots.Ssh.Tools.Common import TerminalModes as terminal_modes

class SshClientBase(URServiceBase):
	'''Provides a client connection to SSH server'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ssh_client_base()
		else:
			self._instance = _internal

	def disconnect(self) -> None:
		'''Disconnects this client from the SSH server'''
		self._instance.Disconnect()

	def create_command(self, commandText: str, encoding: typing.Any) -> SshCommand:
		'''Creates the command to be executed with specified encoding.

		:param commandText: The command text.
		:param encoding: The encoding to use for results.
		:returns: SshCommand object which uses specified encoding.
		'''
		return SshCommand(self._instance.CreateCommand(commandText, encoding))

	def run_command(self, commandText: str) -> SshCommand:
		'''Creates and executes the command.

		:param commandText: The command text.
		:returns: Returns an instance of SshCommand with execution results.
		'''
		return SshCommand(self._instance.RunCommand(commandText))

	def create_shell(self, encoding: typing.Any, input: str, output: typing.Any, extendedOutput: typing.Any, terminalName: str, columns: int, rows: int, width: int, height: int, terminalModes: typing.Any, bufferSize: int) -> Shell:
		return Shell(self._instance.CreateShell(encoding, input, output, extendedOutput, terminalName, columns, rows, width, height, terminalModes, bufferSize))

	def create_shell_stream(self, terminalName: str, columns: int, rows: int, width: int, height: int, bufferSize: int, terminalModeValues: typing.Any) -> ShellStream:
		return ShellStream(self._instance.CreateShellStream(terminalName, columns, rows, width, height, bufferSize, terminalModeValues))

	@property
	def connected(self) -> bool:
		'''Gets a value indicating if this client is connected to the robot'''
		return self._instance.Connected

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SshClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
