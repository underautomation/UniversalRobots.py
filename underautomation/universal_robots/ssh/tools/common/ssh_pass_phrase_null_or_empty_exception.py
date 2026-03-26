import typing
from __future__ import annotation
from underautomation.universal_robots.ssh.tools.common.ssh_exception import SshException
from UnderAutomation.UniversalRobots.Ssh.Tools.Common import SshPassPhraseNullOrEmptyException as ssh_pass_phrase_null_or_empty_exception

class SshPassPhraseNullOrEmptyException(SshException):
	'''The exception that is thrown when pass phrase for key file is empty or null'''
	def __init__(self, message: str, innerException: typing.Any, _internal = 0):
		'''Initializes a new instance of the SshPassPhraseNullOrEmptyException class.

		:param message: The message.
		:param innerException: The inner exception.
		'''
		if(_internal == 0):
			self._instance = ssh_pass_phrase_null_or_empty_exception(message, innerException)
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SshPassPhraseNullOrEmptyException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
