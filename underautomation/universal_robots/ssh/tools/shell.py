from __future__ import annotations
import typing
from underautomation.universal_robots.ssh.tools.common.exception_event_args import ExceptionEventArgs
from UnderAutomation.UniversalRobots.Ssh.Tools import Shell as shell

class Shell:
	'''Represents instance of the SSH shell object'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = shell()
		else:
			self._instance = _internal

	def starting(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.Starting+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def started(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.Started+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def stopping(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.Stopping+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def stopped(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.Stopped+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def error_occurred(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ErrorOccurred+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def start(self) -> None:
		'''Starts this shell.'''
		self._instance.Start()

	def stop(self) -> None:
		'''Stops this shell.'''
		self._instance.Stop()

	def dispose(self) -> None:
		'''Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.'''
		self._instance.Dispose()

	@property
	def is_started(self) -> bool:
		'''Gets a value indicating whether this shell is started.'''
		return self._instance.IsStarted

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Shell):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self._instance.Dispose()
		return False
