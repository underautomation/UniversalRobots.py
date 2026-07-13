from __future__ import annotations
import typing
from underautomation.universal_robots.ssh.tools.common.ssh_exception import SshException
from UnderAutomation.UniversalRobots.Ssh.Tools.Common import SftpPermissionDeniedException as sftp_permission_denied_exception

class SftpPermissionDeniedException(SshException):
	'''The exception that is thrown when operation permission is denied.'''
	def __init__(self, message: str, innerException: typing.Any, _internal = 0):
		'''Initializes a new instance of the SftpPermissionDeniedException class.

		:param message: The message.
		:param innerException: The inner exception.
		'''
		if(_internal == 0):
			self._instance = sftp_permission_denied_exception(message, innerException)
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SftpPermissionDeniedException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
