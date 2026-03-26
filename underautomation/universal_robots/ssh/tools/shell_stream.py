import typing
from __future__ import annotation
from underautomation.universal_robots.ssh.tools.expect_action import ExpectAction
from underautomation.universal_robots.ssh.tools.common.shell_data_event_args import ShellDataEventArgs
from underautomation.universal_robots.ssh.tools.common.exception_event_args import ExceptionEventArgs
from UnderAutomation.UniversalRobots.Ssh.Tools import ShellStream as shell_stream
from System.IO import SeekOrigin as seek_origin

class ShellStream:
	'''Contains operation for working with SSH Shell.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = shell_stream()
		else:
			self._instance = _internal

	def data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.DataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def error_occurred(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ErrorOccurred+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def flush(self) -> None:
		'''Clears all buffers for this stream and causes any buffered data to be written to the underlying device.'''
		self._instance.Flush()

	def read(self, buffer: typing.List[int], offset: int, count: int) -> int:
		'''Reads a sequence of bytes from the current stream and advances the position within the stream by the number of bytes read.

		:param buffer: An array of bytes. When this method returns, the buffer contains the specified byte array with the values between offset and (offset + count - 1) replaced by the bytes read from the current source.
		:param offset: The zero-based byte offset in buffer at which to begin storing the data read from the current stream.
		:param count: The maximum number of bytes to be read from the current stream.
		:returns: The total number of bytes read into the buffer. This can be less than the number of bytes requested if that many bytes are not currently available, or zero (0) if the end of the stream has been reached.
		'''
		return self._instance.Read(buffer, offset, count)

	def seek(self, offset: int, origin: typing.Any) -> int:
		'''This method is not supported.

		:param offset: A byte offset relative to the origin parameter.
		:param origin: A value of type SeekOrigin indicating the reference point used to obtain the new position.
		:returns: The new position within the current stream.
		'''
		return self._instance.Seek(offset, seek_origin(int(origin)))

	def set_length(self, value: int) -> None:
		'''This method is not supported.

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

	def expect(self, regex: typing.Any, timeout: typing.Any) -> str:
		'''Expects the expression specified by regular expression.

		:param regex: The regular expression to expect.
		:param timeout: Time to wait for input.
		:returns: The text available in the shell that contains all the text that ends with expected expression, or null if the specified time has elapsed.
		'''
		return self._instance.Expect(regex, timeout)

	def begin_expect(self, timeout: typing.Any, callback: typing.Any, state: typing.Any, expectActions: typing.List[ExpectAction]) -> typing.Any:
		'''Begins the expect.

		:param timeout: The timeout.
		:param callback: The callback.
		:param state: The state.
		:param expectActions: The expect actions.
		:returns: An IAsyncResult that references the asynchronous operation.
		'''
		return self._instance.BeginExpect(timeout, callback, state, [x._instance if x else None for x in expectActions])

	def end_expect(self, asyncResult: typing.Any) -> str:
		'''Ends the execute.

		:param asyncResult: The async result.
		'''
		return self._instance.EndExpect(asyncResult)

	def read_line(self, timeout: typing.Any) -> str:
		'''Reads a line from the shell. If line is not available it will block the execution and will wait for new line.

		:param timeout: Time to wait for input.
		:returns: The line read from the shell, or null when no input is received for the specified timeout.
		'''
		return self._instance.ReadLine(timeout)

	def write_line(self, line: str) -> None:
		'''Writes the line to the shell.

		:param line: The line to be written to the shell.
		'''
		self._instance.WriteLine(line)

	@property
	def data_available(self) -> bool:
		'''Gets a value that indicates whether data is available on the ShellStream to be read.'''
		return self._instance.DataAvailable

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

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ShellStream):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self._instance.Dispose()
		return False
