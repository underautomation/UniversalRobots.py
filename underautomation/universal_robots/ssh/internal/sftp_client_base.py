from __future__ import annotations
import typing
from underautomation.universal_robots.ssh.tools.sftp.sftp_file import SftpFile
from underautomation.universal_robots.ssh.tools.sftp.sftp_file_sytem_information import SftpFileSytemInformation
from underautomation.universal_robots.ssh.tools.sftp.sftp_file_stream import SftpFileStream
from datetime import datetime, timedelta
from underautomation.universal_robots.ssh.tools.sftp.sftp_file_attributes import SftpFileAttributes
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from UnderAutomation.UniversalRobots.Ssh.Internal import SftpClientBase as sftp_client_base
from System.IO import FileMode as file_mode
from System.IO import FileAccess as file_access

class SftpClientBase(URServiceBase):
	'''Implementation of the SSH File Transfer Protocol (SFTP) over SSH for transfering files to the robot controller'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sftp_client_base()
		else:
			self._instance = _internal

	def disconnect(self) -> None:
		'''Disconnects this client from the SFTP server.'''
		self._instance.Disconnect()

	def change_directory(self, path: str) -> None:
		'''Changes remote directory to path.

		:param path: New directory path.
		'''
		self._instance.ChangeDirectory(path)

	def change_permissions(self, path: str, mode: int) -> None:
		'''Changes permissions of file(s) to specified mode.

		:param path: File(s) path, may match multiple files.
		:param mode: The mode.
		'''
		self._instance.ChangePermissions(path, mode)

	def create_directory(self, path: str) -> None:
		'''Creates remote directory specified by path.

		:param path: Directory path to create.
		'''
		self._instance.CreateDirectory(path)

	def delete_directory(self, path: str) -> None:
		'''Deletes remote directory specified by path.

		:param path: Directory to be deleted path.
		'''
		self._instance.DeleteDirectory(path)

	def delete_file(self, path: str) -> None:
		'''Deletes remote file specified by path.

		:param path: File to be deleted path.
		'''
		self._instance.DeleteFile(path)

	def rename_file(self, oldPath: str, newPath: str, isPosix: bool) -> None:
		'''Renames remote file from old path to new path.

		:param oldPath: Path to the old file location.
		:param newPath: Path to the new file location.
		:param isPosix: if set to true then perform a posix rename.
		'''
		self._instance.RenameFile(oldPath, newPath, isPosix)

	def symbolic_link(self, path: str, linkPath: str) -> None:
		'''Creates a symbolic link from old path to new path.

		:param path: The old path.
		:param linkPath: The new path.
		'''
		self._instance.SymbolicLink(path, linkPath)

	def enumerate_programs(self) -> typing.List[str]:
		'''Enumerates programs with .urp extension. It searches recursively programs in "/programs" if it exists, or "/home/ur/ursim-current/programs" for simulator

		:returns: Array of program relative path
		'''
		return self._instance.EnumeratePrograms()

	def enumerate_installations(self) -> typing.List[str]:
		'''Enumerates installations with .installation extension. It searches recursively installations in "/programs" if it exists, or "/home/ur/ursim-current/programs" for simulator

		:returns: Array of installations relative path
		'''
		return self._instance.EnumerateInstallations()

	def get(self, path: str) -> SftpFile:
		'''Gets reference to remote file or directory.

		:param path: The path.
		:returns: A reference to SftpFile file object.
		'''
		return SftpFile(self._instance.Get(path))

	def exists(self, path: str) -> bool:
		'''Checks whether file or directory exists;

		:param path: The path.
		:returns: true if directory or file exists; otherwise false.
		'''
		return self._instance.Exists(path)

	def get_status(self, path: str) -> SftpFileSytemInformation:
		'''Gets status using statvfs@openssh.com request.

		:param path: The path.
		:returns: A SftpFileSytemInformation instance that contains file status information.
		'''
		return SftpFileSytemInformation(self._instance.GetStatus(path))

	def create(self, path: str, bufferSize: int) -> SftpFileStream:
		'''Creates or overwrites the specified file.

		:param path: The path and name of the file to create.
		:param bufferSize: The maximum number of bytes buffered for reads and writes to the file.
		:returns: A SftpFileStream that provides read/write access to the file specified in path.
		'''
		return SftpFileStream(self._instance.Create(path, bufferSize))

	def delete(self, path: str) -> None:
		'''Deletes the specified file or directory.

		:param path: The name of the file or directory to be deleted. Wildcard characters are not supported.
		'''
		self._instance.Delete(path)

	def get_last_access_time(self, path: str) -> datetime:
		'''Returns the date and time the specified file or directory was last accessed.

		:param path: The file or directory for which to obtain access date and time information.
		:returns: A DateTime structure set to the date and time that the specified file or directory was last accessed. This value is expressed in local time.
		'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.GetLastAccessTime(path).Ticks // 10)

	def get_last_access_time_utc(self, path: str) -> datetime:
		'''Returns the date and time, in coordinated universal time (UTC), that the specified file or directory was last accessed.

		:param path: The file or directory for which to obtain access date and time information.
		:returns: A DateTime structure set to the date and time that the specified file or directory was last accessed. This value is expressed in UTC time.
		'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.GetLastAccessTimeUtc(path).Ticks // 10)

	def get_last_write_time(self, path: str) -> datetime:
		'''Returns the date and time the specified file or directory was last written to.

		:param path: The file or directory for which to obtain write date and time information.
		:returns: A DateTime structure set to the date and time that the specified file or directory was last written to. This value is expressed in local time.
		'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.GetLastWriteTime(path).Ticks // 10)

	def get_last_write_time_utc(self, path: str) -> datetime:
		'''Returns the date and time, in coordinated universal time (UTC), that the specified file or directory was last written to.

		:param path: The file or directory for which to obtain write date and time information.
		:returns: A DateTime structure set to the date and time that the specified file or directory was last written to. This value is expressed in UTC time.
		'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.GetLastWriteTimeUtc(path).Ticks // 10)

	def open_read(self, path: str) -> SftpFileStream:
		'''Opens an existing file for reading.

		:param path: The file to be opened for reading.
		:returns: A read-only SftpFileStream on the specified path.
		'''
		return SftpFileStream(self._instance.OpenRead(path))

	def open_write(self, path: str) -> SftpFileStream:
		'''Opens a file for writing.

		:param path: The file to be opened for writing.
		:returns: An unshared SftpFileStream object on the specified path with Write access.
		'''
		return SftpFileStream(self._instance.OpenWrite(path))

	def read_all_bytes(self, path: str) -> typing.List[int]:
		'''Opens a binary file, reads the contents of the file into a byte array, and closes the file.

		:param path: The file to open for reading.
		:returns: A byte array containing the contents of the file.
		'''
		return self._instance.ReadAllBytes(path)

	def write_all_bytes(self, path: str, bytes: typing.List[int]) -> None:
		'''Writes the specified byte array to the specified file, and closes the file.

		:param path: The file to write to.
		:param bytes: The bytes to write to the file.
		'''
		self._instance.WriteAllBytes(path, bytes)

	def write_all_lines(self, path: str, contents: typing.List[str]) -> None:
		'''Writes a collection of strings to the file using the UTF-8 encoding, and closes the file.

		:param path: The file to write to.
		:param contents: The lines to write to the file.
		'''
		self._instance.WriteAllLines(path, contents)

	def get_attributes(self, path: str) -> SftpFileAttributes:
		'''Gets the SftpFileAttributes of the file on the path.

		:param path: The path to the file.
		:returns: The SftpFileAttributes of the file on the path.
		'''
		return SftpFileAttributes(self._instance.GetAttributes(path))

	def set_attributes(self, path: str, fileAttributes: SftpFileAttributes) -> None:
		'''Sets the specified SftpFileAttributes of the file on the specified path.

		:param path: The path to the file.
		:param fileAttributes: The desired SftpFileAttributes.
		'''
		self._instance.SetAttributes(path, fileAttributes._instance if fileAttributes else None)

	@property
	def connected(self) -> bool:
		'''Gets a value indicating if this client is connected to the robot'''
		return self._instance.Connected

	@property
	def operation_timeout(self) -> typing.Any:
		'''Gets or sets the operation timeout.'''
		return self._instance.OperationTimeout

	@operation_timeout.setter
	def operation_timeout(self, value: typing.Any):
		self._instance.OperationTimeout = value

	@property
	def buffer_size(self) -> int:
		'''Gets or sets the maximum size of the buffer in bytes.'''
		return self._instance.BufferSize

	@buffer_size.setter
	def buffer_size(self, value: int):
		self._instance.BufferSize = value

	@property
	def working_directory(self) -> str:
		'''Gets remote working directory.'''
		return self._instance.WorkingDirectory

	@property
	def protocol_version(self) -> int:
		'''Gets sftp protocol version.'''
		return self._instance.ProtocolVersion

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SftpClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
