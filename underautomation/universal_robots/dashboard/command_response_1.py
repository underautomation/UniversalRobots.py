from __future__ import annotations
import typing
from underautomation.universal_robots.dashboard.command_response import CommandResponse
from UnderAutomation.UniversalRobots.Dashboard import CommandResponse as command_response_1

T = typing.TypeVar('T')
class CommandResponse1(CommandResponse, typing.Generic[T]):
	'''Answer returned by a command which contains a typed value.'''
	def __init__(self, command: CommandResponse, _internal = 0):
		'''Initializes a new instance of CommandResponse`1 by copying the base response data.

		:param command: The base command response to copy from.
		'''
		if(_internal == 0):
			self._instance = command_response_1(command._instance if command else None)
		else:
			self._instance = _internal

	@property
	def value(self) -> T:
		'''Value return by the command'''
		return self._instance.Value

	@value.setter
	def value(self, value: T):
		self._instance.Value = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CommandResponse1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
