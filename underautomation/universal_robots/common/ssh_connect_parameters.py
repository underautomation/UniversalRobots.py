from __future__ import annotations
import typing
from underautomation.universal_robots.ssh.internal.ssh_parameters_base import SshParametersBase
from UnderAutomation.UniversalRobots.Common import SshConnectParameters as ssh_connect_parameters

class SshConnectParameters(SshParametersBase):
	'''Setup SSH client'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ssh_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable_ssh(self) -> bool:
		'''Choose to enable SSH command line client Default value is false'''
		return self._instance.EnableSsh

	@enable_ssh.setter
	def enable_ssh(self, value: bool):
		self._instance.EnableSsh = value

	@property
	def enable_sftp(self) -> bool:
		'''Choose to enable FTP Default value is false'''
		return self._instance.EnableSftp

	@enable_sftp.setter
	def enable_sftp(self, value: bool):
		self._instance.EnableSftp = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SshConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
