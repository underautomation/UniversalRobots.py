import typing
from __future__ import annotation
from underautomation.universal_robots.ssh.internal.sftp_client_base import SftpClientBase
from UnderAutomation.UniversalRobots.Internal import SftpClientInternal as sftp_client_internal

class SftpClientInternal(SftpClientBase):
	'''Implementation of the SSH File Transfer Protocol (SFTP) over SSH for transfering files to the robot controller'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sftp_client_internal()
		else:
			self._instance = _internal

	def connect(self, port: int, username: str, password: str) -> None:
		'''Connects to Sftp robot server

		:param port: SFTP port to connect to
		:param username: Robot linux username (default username is admin)
		:param password: Associated user password (default is easybot)
		'''
		self._instance.Connect(port, username, password)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SftpClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
