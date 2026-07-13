from __future__ import annotations
import typing
from underautomation.universal_robots.ssh.internal.ssh_client_base import SshClientBase
from UnderAutomation.UniversalRobots.Internal import SshClientInternal as ssh_client_internal

class SshClientInternal(SshClientBase):
	'''Provides a client connection to SSH server'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ssh_client_internal()
		else:
			self._instance = _internal

	def connect(self, port: int, username: str, password: str) -> None:
		'''Connects to the SSH robot server

		:param port: SSH port number.
		:param username: Robot linux username (default username is admin)
		:param password: Associated user password (default is easybot)
		'''
		self._instance.Connect(port, username, password)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SshClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
