from __future__ import annotations
import typing
from underautomation.universal_robots.common.status_code import StatusCode
from UnderAutomation.UniversalRobots.Common import InternalErrorEventArgs as internal_error_event_args
from UnderAutomation.UniversalRobots.Common import StatusCode as status_code

class InternalErrorEventArgs:
	'''Describes an internal error'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = internal_error_event_args()
		else:
			self._instance = _internal

	@property
	def exception(self) -> typing.Any:
		'''The exception thrown that causes an internal error'''
		return self._instance.Exception

	@property
	def message(self) -> str:
		'''Explicit message that explains what happened'''
		return self._instance.Message

	@property
	def status(self) -> StatusCode:
		'''Context status associated to this internal error'''
		return StatusCode(int(self._instance.Status))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, InternalErrorEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
