import typing
from __future__ import annotation
from datetime import datetime, timedelta
from UnderAutomation.UniversalRobots.Ssh.Tools.Sftp import SftpFileAttributes as sftp_file_attributes

class SftpFileAttributes:
	'''Contains SFTP file attributes.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sftp_file_attributes()
		else:
			self._instance = _internal

	def set_permissions(self, mode: int) -> None:
		'''Sets the permissions.

		:param mode: The mode.
		'''
		self._instance.SetPermissions(mode)

	def get_bytes(self) -> typing.List[int]:
		'''Returns a byte array representing the current SftpFileAttributes.

		:returns: A byte array representing the current SftpFileAttributes.
		'''
		return self._instance.GetBytes()

	@property
	def last_access_time(self) -> datetime:
		'''Gets or sets the local time the current file or directory was last accessed.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.LastAccessTime.Ticks // 10)

	@last_access_time.setter
	def last_access_time(self, value: datetime):
		self._instance.LastAccessTime = value

	@property
	def last_write_time(self) -> datetime:
		'''Gets or sets the local time when the current file or directory was last written to.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.LastWriteTime.Ticks // 10)

	@last_write_time.setter
	def last_write_time(self, value: datetime):
		self._instance.LastWriteTime = value

	@property
	def last_access_time_utc(self) -> datetime:
		'''Gets or sets the UTC time the current file or directory was last accessed.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.LastAccessTimeUtc.Ticks // 10)

	@last_access_time_utc.setter
	def last_access_time_utc(self, value: datetime):
		self._instance.LastAccessTimeUtc = value

	@property
	def last_write_time_utc(self) -> datetime:
		'''Gets or sets the UTC time when the current file or directory was last written to.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.LastWriteTimeUtc.Ticks // 10)

	@last_write_time_utc.setter
	def last_write_time_utc(self, value: datetime):
		self._instance.LastWriteTimeUtc = value

	@property
	def size(self) -> int:
		'''Gets or sets the size, in bytes, of the current file.'''
		return self._instance.Size

	@size.setter
	def size(self, value: int):
		self._instance.Size = value

	@property
	def user_id(self) -> int:
		'''Gets or sets file user id.'''
		return self._instance.UserId

	@user_id.setter
	def user_id(self, value: int):
		self._instance.UserId = value

	@property
	def group_id(self) -> int:
		'''Gets or sets file group id.'''
		return self._instance.GroupId

	@group_id.setter
	def group_id(self, value: int):
		self._instance.GroupId = value

	@property
	def is_socket(self) -> bool:
		'''Gets a value indicating whether file represents a socket.'''
		return self._instance.IsSocket

	@property
	def is_symbolic_link(self) -> bool:
		'''Gets a value indicating whether file represents a symbolic link.'''
		return self._instance.IsSymbolicLink

	@property
	def is_regular_file(self) -> bool:
		'''Gets a value indicating whether file represents a regular file.'''
		return self._instance.IsRegularFile

	@property
	def is_block_device(self) -> bool:
		'''Gets a value indicating whether file represents a block device.'''
		return self._instance.IsBlockDevice

	@property
	def is_directory(self) -> bool:
		'''Gets a value indicating whether file represents a directory.'''
		return self._instance.IsDirectory

	@property
	def is_character_device(self) -> bool:
		'''Gets a value indicating whether file represents a character device.'''
		return self._instance.IsCharacterDevice

	@property
	def is_named_pipe(self) -> bool:
		'''Gets a value indicating whether file represents a named pipe.'''
		return self._instance.IsNamedPipe

	@property
	def owner_can_read(self) -> bool:
		'''Gets a value indicating whether the owner can read from this file.'''
		return self._instance.OwnerCanRead

	@owner_can_read.setter
	def owner_can_read(self, value: bool):
		self._instance.OwnerCanRead = value

	@property
	def owner_can_write(self) -> bool:
		'''Gets a value indicating whether the owner can write into this file.'''
		return self._instance.OwnerCanWrite

	@owner_can_write.setter
	def owner_can_write(self, value: bool):
		self._instance.OwnerCanWrite = value

	@property
	def owner_can_execute(self) -> bool:
		'''Gets a value indicating whether the owner can execute this file.'''
		return self._instance.OwnerCanExecute

	@owner_can_execute.setter
	def owner_can_execute(self, value: bool):
		self._instance.OwnerCanExecute = value

	@property
	def group_can_read(self) -> bool:
		'''Gets a value indicating whether the group members can read from this file.'''
		return self._instance.GroupCanRead

	@group_can_read.setter
	def group_can_read(self, value: bool):
		self._instance.GroupCanRead = value

	@property
	def group_can_write(self) -> bool:
		'''Gets a value indicating whether the group members can write into this file.'''
		return self._instance.GroupCanWrite

	@group_can_write.setter
	def group_can_write(self, value: bool):
		self._instance.GroupCanWrite = value

	@property
	def group_can_execute(self) -> bool:
		'''Gets a value indicating whether the group members can execute this file.'''
		return self._instance.GroupCanExecute

	@group_can_execute.setter
	def group_can_execute(self, value: bool):
		self._instance.GroupCanExecute = value

	@property
	def others_can_read(self) -> bool:
		'''Gets a value indicating whether the others can read from this file.'''
		return self._instance.OthersCanRead

	@others_can_read.setter
	def others_can_read(self, value: bool):
		self._instance.OthersCanRead = value

	@property
	def others_can_write(self) -> bool:
		'''Gets a value indicating whether the others can write into this file.'''
		return self._instance.OthersCanWrite

	@others_can_write.setter
	def others_can_write(self, value: bool):
		self._instance.OthersCanWrite = value

	@property
	def others_can_execute(self) -> bool:
		'''Gets a value indicating whether the others can execute this file.'''
		return self._instance.OthersCanExecute

	@others_can_execute.setter
	def others_can_execute(self, value: bool):
		self._instance.OthersCanExecute = value

	@property
	def extensions(self) -> typing.Any:
		'''Gets or sets the extensions.'''
		return self._instance.Extensions

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SftpFileAttributes):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
