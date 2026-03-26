import typing
from __future__ import annotation
from underautomation.universal_robots.ssh.tools.sftp.sftp_file_attributes import SftpFileAttributes
from datetime import datetime, timedelta
from UnderAutomation.UniversalRobots.Ssh.Tools.Sftp import SftpFile as sftp_file

class SftpFile:
	'''Represents SFTP file information'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sftp_file()
		else:
			self._instance = _internal

	def set_permissions(self, mode: int) -> None:
		'''Sets file permissions.

		:param mode: The mode.
		'''
		self._instance.SetPermissions(mode)

	def delete(self) -> None:
		'''Permanently deletes a file on remote machine.'''
		self._instance.Delete()

	def move_to(self, destFileName: str) -> None:
		'''Moves a specified file to a new location on remote machine, providing the option to specify a new file name.

		:param destFileName: The path to move the file to, which can specify a different file name.
		'''
		self._instance.MoveTo(destFileName)

	def update_status(self) -> None:
		'''Updates file status on the server.'''
		self._instance.UpdateStatus()

	@property
	def attributes(self) -> SftpFileAttributes:
		'''Gets the file attributes.'''
		return SftpFileAttributes(self._instance.Attributes)

	@property
	def full_name(self) -> str:
		'''Gets the full path of the directory or file.'''
		return self._instance.FullName

	@property
	def name(self) -> str:
		'''For files, gets the name of the file. For directories, gets the name of the last directory in the hierarchy if a hierarchy exists. Otherwise, the Name property gets the name of the directory.'''
		return self._instance.Name

	@property
	def last_access_time(self) -> datetime:
		'''Gets or sets the time the current file or directory was last accessed.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.LastAccessTime.Ticks // 10)

	@last_access_time.setter
	def last_access_time(self, value: datetime):
		self._instance.LastAccessTime = value

	@property
	def last_write_time(self) -> datetime:
		'''Gets or sets the time when the current file or directory was last written to.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.LastWriteTime.Ticks // 10)

	@last_write_time.setter
	def last_write_time(self, value: datetime):
		self._instance.LastWriteTime = value

	@property
	def last_access_time_utc(self) -> datetime:
		'''Gets or sets the time, in coordinated universal time (UTC), the current file or directory was last accessed.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.LastAccessTimeUtc.Ticks // 10)

	@last_access_time_utc.setter
	def last_access_time_utc(self, value: datetime):
		self._instance.LastAccessTimeUtc = value

	@property
	def last_write_time_utc(self) -> datetime:
		'''Gets or sets the time, in coordinated universal time (UTC), when the current file or directory was last written to.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.LastWriteTimeUtc.Ticks // 10)

	@last_write_time_utc.setter
	def last_write_time_utc(self, value: datetime):
		self._instance.LastWriteTimeUtc = value

	@property
	def length(self) -> int:
		'''Gets or sets the size, in bytes, of the current file.'''
		return self._instance.Length

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
		'''Gets or sets a value indicating whether the owner can read from this file.'''
		return self._instance.OwnerCanRead

	@owner_can_read.setter
	def owner_can_read(self, value: bool):
		self._instance.OwnerCanRead = value

	@property
	def owner_can_write(self) -> bool:
		'''Gets or sets a value indicating whether the owner can write into this file.'''
		return self._instance.OwnerCanWrite

	@owner_can_write.setter
	def owner_can_write(self, value: bool):
		self._instance.OwnerCanWrite = value

	@property
	def owner_can_execute(self) -> bool:
		'''Gets or sets a value indicating whether the owner can execute this file.'''
		return self._instance.OwnerCanExecute

	@owner_can_execute.setter
	def owner_can_execute(self, value: bool):
		self._instance.OwnerCanExecute = value

	@property
	def group_can_read(self) -> bool:
		'''Gets or sets a value indicating whether the group members can read from this file.'''
		return self._instance.GroupCanRead

	@group_can_read.setter
	def group_can_read(self, value: bool):
		self._instance.GroupCanRead = value

	@property
	def group_can_write(self) -> bool:
		'''Gets or sets a value indicating whether the group members can write into this file.'''
		return self._instance.GroupCanWrite

	@group_can_write.setter
	def group_can_write(self, value: bool):
		self._instance.GroupCanWrite = value

	@property
	def group_can_execute(self) -> bool:
		'''Gets or sets a value indicating whether the group members can execute this file.'''
		return self._instance.GroupCanExecute

	@group_can_execute.setter
	def group_can_execute(self, value: bool):
		self._instance.GroupCanExecute = value

	@property
	def others_can_read(self) -> bool:
		'''Gets or sets a value indicating whether the others can read from this file.'''
		return self._instance.OthersCanRead

	@others_can_read.setter
	def others_can_read(self, value: bool):
		self._instance.OthersCanRead = value

	@property
	def others_can_write(self) -> bool:
		'''Gets or sets a value indicating whether the others can write into this file.'''
		return self._instance.OthersCanWrite

	@others_can_write.setter
	def others_can_write(self, value: bool):
		self._instance.OthersCanWrite = value

	@property
	def others_can_execute(self) -> bool:
		'''Gets or sets a value indicating whether the others can execute this file.'''
		return self._instance.OthersCanExecute

	@others_can_execute.setter
	def others_can_execute(self, value: bool):
		self._instance.OthersCanExecute = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SftpFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
