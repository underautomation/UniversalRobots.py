from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Dashboard import CommandResponse as command_response

class CommandResponse:
	'''Generic answer returned by a command'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = command_response()
		else:
			self._instance = _internal

	@property
	def succeed(self) -> bool:
		'''The command as succeeded'''
		return self._instance.Succeed

	@succeed.setter
	def succeed(self, value: bool):
		self._instance.Succeed = value

	@property
	def message(self) -> str:
		'''A message that described the error or the action done'''
		return self._instance.Message

	@message.setter
	def message(self, value: str):
		self._instance.Message = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CommandResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
