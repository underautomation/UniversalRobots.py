from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Ssh.Tools.Common import SshException as ssh_exception

class SshException:
	'''The exception that is thrown when SSH exception occurs.'''
	def __init__(self, message: str, inner: typing.Any, _internal = 0):
		'''Initializes a new instance of the SshException class.

		:param message: The message.
		:param inner: The inner.
		'''
		if(_internal == 0):
			self._instance = ssh_exception(message, inner)
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SshException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
