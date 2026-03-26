import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Ssh.Tools.Common import ExceptionEventArgs as exception_event_args

class ExceptionEventArgs:
	'''Provides data for the ErrorOccured events.'''
	def __init__(self, exception: typing.Any, _internal = 0):
		'''Initializes a new instance of the ExceptionEventArgs class.

		:param exception: An System.Exception that represents the error that occurred.
		'''
		if(_internal == 0):
			self._instance = exception_event_args(exception)
		else:
			self._instance = _internal

	@property
	def exception(self) -> typing.Any:
		'''Gets the System.Exception that represents the error that occurred.'''
		return self._instance.Exception

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ExceptionEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
