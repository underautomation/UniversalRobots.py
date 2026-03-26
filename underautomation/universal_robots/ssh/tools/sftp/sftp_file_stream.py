import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Ssh.Tools.Sftp import SftpFileStream as sftp_file_stream
from System.IO import SeekOrigin as seek_origin

class SftpFileStream:
	'''Exposes a Stream around a remote SFTP file, supporting both synchronous and asynchronous read and write operations.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sftp_file_stream()
		else:
			self._instance = _internal

	def flush(self) -> None:
		'''Clears all buffers for this stream and causes any buffered data to be written to the file.'''
		self._instance.Flush()

	def read(self, buffer: typing.List[int], offset: int, count: int) -> int:
		'''Reads a sequence of bytes from the current stream and advances the position within the stream by the number of bytes read.

		:param buffer: An array of bytes. When this method returns, the buffer contains the specified byte array with the values between offset and (offset + count - 1) replaced by the bytes read from the current source.
		:param offset: The zero-based byte offset in buffer at which to begin storing the data read from the current stream.
		:param count: The maximum number of bytes to be read from the current stream.
		:returns: The total number of bytes read into the buffer. This can be less than the number of bytes requested if that many bytes are not currently available, or zero (0) if the end of the stream has been reached.
		'''
		return self._instance.Read(buffer, offset, count)

	def read_byte(self) -> int:
		'''Reads a byte from the stream and advances the position within the stream by one byte, or returns -1 if at the end of the stream.

		:returns: The unsigned byte cast to an Int32, or -1 if at the end of the stream.
		'''
		return self._instance.ReadByte()

	def seek(self, offset: int, origin: typing.Any) -> int:
		'''Sets the position within the current stream.

		:param offset: A byte offset relative to the origin parameter.
		:param origin: A value of type SeekOrigin indicating the reference point used to obtain the new position.
		:returns: The new position within the current stream.
		'''
		return self._instance.Seek(offset, seek_origin(int(origin)))

	def set_length(self, value: int) -> None:
		'''Sets the length of the current stream.

		:param value: The desired length of the current stream in bytes.
		'''
		self._instance.SetLength(value)

	def write(self, buffer: typing.List[int], offset: int, count: int) -> None:
		'''Writes a sequence of bytes to the current stream and advances the current position within this stream by the number of bytes written.

		:param buffer: An array of bytes. This method copies count bytes from buffer to the current stream.
		:param offset: The zero-based byte offset in buffer at which to begin copying bytes to the current stream.
		:param count: The number of bytes to be written to the current stream.
		'''
		self._instance.Write(buffer, offset, count)

	def write_byte(self, value: int) -> None:
		'''Writes a byte to the current position in the stream and advances the position within the stream by one byte.

		:param value: The byte to write to the stream.
		'''
		self._instance.WriteByte(value)

	@property
	def can_read(self) -> bool:
		'''Gets a value indicating whether the current stream supports reading.'''
		return self._instance.CanRead

	@property
	def can_seek(self) -> bool:
		'''Gets a value indicating whether the current stream supports seeking.'''
		return self._instance.CanSeek

	@property
	def can_write(self) -> bool:
		'''Gets a value indicating whether the current stream supports writing.'''
		return self._instance.CanWrite

	@property
	def can_timeout(self) -> bool:
		'''Indicates whether timeout properties are usable for SftpFileStream.'''
		return self._instance.CanTimeout

	@property
	def length(self) -> int:
		'''Gets the length in bytes of the stream.'''
		return self._instance.Length

	@property
	def position(self) -> int:
		'''Gets or sets the position within the current stream.'''
		return self._instance.Position

	@position.setter
	def position(self, value: int):
		self._instance.Position = value

	@property
	def name(self) -> str:
		'''Gets the name of the path that was used to construct the current SftpFileStream.'''
		return self._instance.Name

	@property
	def handle(self) -> typing.List[int]:
		'''Gets the operating system file handle for the file that the current SftpFileStream encapsulates.'''
		return self._instance.Handle

	@property
	def timeout(self) -> typing.Any:
		'''Gets or sets the operation timeout.'''
		return self._instance.Timeout

	@timeout.setter
	def timeout(self, value: typing.Any):
		self._instance.Timeout = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SftpFileStream):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self._instance.Dispose()
		return False
