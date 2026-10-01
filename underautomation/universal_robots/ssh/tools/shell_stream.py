from __future__ import annotations
import typing
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

	@typing.overload
	def read(self, buffer: typing.List[int], offset: int, count: int) -> int: ...

	@typing.overload
	def read(self) -> str: ...

	def read(self, *args, **kwargs) -> int | str:
		'''Reads a sequence of bytes from the current stream and advances the position within the stream by the number of bytes read.
		Reads text available in the shell.

		Arguments: (buffer, offset, count)
		Arguments: ()
		:param buffer: An array of bytes. When this method returns, the buffer contains the specified byte array with the values between offset and (offset + count - 1) replaced by the bytes read from the current source.
		:param offset: The zero-based byte offset in buffer at which to begin storing the data read from the current stream.
		:param count: The maximum number of bytes to be read from the current stream.
		:returns: The total number of bytes read into the buffer. This can be less than the number of bytes requested if that many bytes are not currently available, or zero (0) if the end of the stream has been reached.
		'''
		__a = _bind_overload(args, kwargs, ['buffer', 'offset', 'count'], {})
		if __a is not None:
			buffer, offset, count = __a
			return self._instance.Read(buffer, offset, count)
		__a = _bind_overload(args, kwargs, [], {})
		if __a is not None:
			return self._instance.Read()
		raise TypeError("read(): no overload takes these arguments")

	def set_length(self, value: int) -> None:
		'''This method is not supported.

		:param value: The desired length of the current stream in bytes.
		'''
		self._instance.SetLength(value)

	@typing.overload
	def write(self, buffer: typing.List[int], offset: int, count: int) -> None: ...

	@typing.overload
	def write(self, text: str) -> None: ...

	def write(self, *args, **kwargs) -> None:
		'''Writes a sequence of bytes to the current stream and advances the current position within this stream by the number of bytes written.
		Writes the specified text to the shell.

		Arguments: (buffer, offset, count)
		Arguments: (text)
		:param buffer: An array of bytes. This method copies count bytes from buffer to the current stream.
		:param offset: The zero-based byte offset in buffer at which to begin copying bytes to the current stream.
		:param count: The number of bytes to be written to the current stream.
		:param text: The text to be written to the shell.
		'''
		__a = _bind_overload(args, kwargs, ['buffer', 'offset', 'count'], {})
		if __a is not None:
			buffer, offset, count = __a
			self._instance.Write(buffer, offset, count)
			return
		__a = _bind_overload(args, kwargs, ['text'], {})
		if __a is not None:
			text, = __a
			self._instance.Write(text)
			return
		raise TypeError("write(): no overload takes these arguments")

	def expect(self, expectActions_or_text: str | typing.List[ExpectAction]) -> str | None:
		'''Expects the expression specified by text.
		Expects the specified expression and performs action when one is found.

		:param expectActions_or_text: The text to expect. Or: The expected expressions and actions to perform.
		:returns: Text available in the shell that ends with expected text.
		'''
		return self._instance.Expect(getattr(expectActions_or_text, '_instance', expectActions_or_text))

	def read_line(self) -> str:
		'''Reads the line from the shell. If line is not available it will block the execution and will wait for new line.

		:returns: The line read from the shell.
		'''
		return self._instance.ReadLine()

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

def _bind_overload(args, kwargs, names, defaults):
	if len(args) > len(names) or any(k not in names[len(args):] for k in kwargs):
		return None
	values = list(args)
	for name in names[len(args):]:
		if name in kwargs:
			values.append(kwargs[name])
		elif name in defaults:
			values.append(defaults[name])
		else:
			return None
	return values
