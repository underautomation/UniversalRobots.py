import typing
from __future__ import annotation
from underautomation.universal_robots.ssh.internal.ssh_client_base import SshClientBase
from UnderAutomation.UniversalRobots.Ssh import SshClient as ssh_client

class SshClient(SshClientBase):
	'''Provides a client connection to SSH server'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ssh_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, username: str, password: str, port: int=22) -> None:
		'''Connects to the robot

		:param ip: Robot IP address
		:param username: Robot linux username (default username is ur for simulator and root for real robot)
		:param password: Associated user password (default is easybot)
		:param port: SSH port
		'''
		self._instance.Connect(ip, username, password, port)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SshClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
