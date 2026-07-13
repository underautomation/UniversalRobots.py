from __future__ import annotations
import typing
from underautomation.universal_robots.ssh.tools.common.ssh_exception import SshException
from UnderAutomation.UniversalRobots.Ssh.Tools.Common import SshOperationTimeoutException as ssh_operation_timeout_exception

class SshOperationTimeoutException(SshException):
	'''The exception that is thrown when operation is timed out.'''
	def __init__(self, message: str, innerException: typing.Any, _internal = 0):
		'''Initializes a new instance of the SshOperationTimeoutException class.

		:param message: The message.
		:param innerException: The inner exception.
		'''
		if(_internal == 0):
			self._instance = ssh_operation_timeout_exception(message, innerException)
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SshOperationTimeoutException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
