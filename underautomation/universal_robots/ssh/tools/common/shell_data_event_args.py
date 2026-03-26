import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Ssh.Tools.Common import ShellDataEventArgs as shell_data_event_args

class ShellDataEventArgs:
	'''Provides data for Shell DataReceived event'''
	def __init__(self, data: typing.List[int], _internal = 0):
		'''Initializes a new instance of the ShellDataEventArgs class.

		:param data: The data.
		'''
		if(_internal == 0):
			self._instance = shell_data_event_args(data)
		else:
			self._instance = _internal

	@property
	def data(self) -> typing.List[int]:
		'''Gets the data.'''
		return self._instance.Data

	@property
	def line(self) -> str:
		'''Gets the line data.'''
		return self._instance.Line

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ShellDataEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
