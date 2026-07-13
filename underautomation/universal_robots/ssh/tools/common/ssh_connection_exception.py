from __future__ import annotations
import typing
from underautomation.universal_robots.ssh.tools.messages.transport.disconnect_reason import DisconnectReason
from underautomation.universal_robots.ssh.tools.common.ssh_exception import SshException
from UnderAutomation.UniversalRobots.Ssh.Tools.Common import SshConnectionException as ssh_connection_exception
from UnderAutomation.UniversalRobots.Ssh.Tools.Messages.Transport import DisconnectReason as disconnect_reason

class SshConnectionException(SshException):
	'''The exception that is thrown when connection was terminated.'''
	def __init__(self, message: str, disconnectReasonCode: DisconnectReason, inner: typing.Any, _internal = 0):
		'''Initializes a new instance of the SshConnectionException class.

		:param message: The message.
		:param disconnectReasonCode: The disconnect reason code.
		:param inner: The inner.
		'''
		if(_internal == 0):
			self._instance = ssh_connection_exception(message, disconnect_reason(int(disconnectReasonCode)), inner)
		else:
			self._instance = _internal

	@property
	def disconnect_reason(self) -> DisconnectReason:
		'''Gets the disconnect reason if provided by the server or client. Otherwise None.'''
		return DisconnectReason(int(self._instance.DisconnectReason))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SshConnectionException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
