import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.PrimaryInterface import ProgramThread as program_thread

class ProgramThread:
	'''Represents a single running thread in a UR program.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = program_thread()
		else:
			self._instance = _internal

	@property
	def line_number(self) -> int:
		'''Current line number being executed in the program.'''
		return self._instance.LineNumber

	@line_number.setter
	def line_number(self, value: int):
		self._instance.LineNumber = value

	@property
	def line_name(self) -> str:
		'''Name of the program line being executed.'''
		return self._instance.LineName

	@line_name.setter
	def line_name(self, value: str):
		self._instance.LineName = value

	@property
	def thread_name(self) -> str:
		'''Name of the thread.'''
		return self._instance.ThreadName

	@thread_name.setter
	def thread_name(self, value: str):
		self._instance.ThreadName = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ProgramThread):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
