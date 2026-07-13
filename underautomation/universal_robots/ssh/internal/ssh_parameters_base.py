from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Ssh.Internal import SshParametersBase as ssh_parameters_base

class SshParametersBase:
	'''Base class for SSH and SFTP connection parameters, including credentials and port configuration.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ssh_parameters_base()
		else:
			self._instance = _internal

	@property
	def username(self) -> str:
		'''Setup Linux Username for SSH connection Default value is "ur" for simulator and "root" for real robot'''
		return self._instance.Username

	@username.setter
	def username(self, value: str):
		self._instance.Username = value

	@property
	def password(self) -> str:
		'''Setup Linux Password for SSH connection Default value is "easybot"'''
		return self._instance.Password

	@password.setter
	def password(self, value: str):
		self._instance.Password = value

	@property
	def port(self) -> int:
		'''SSH and SFTP TCP port. Default : 22'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SshParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default SSH server TCP port
SshParametersBase.DEFAULT_PORT = ssh_parameters_base.DEFAULT_PORT
