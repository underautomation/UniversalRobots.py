from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Dashboard import ProgramSaveState as program_save_state

class ProgramSaveState:
	'''Represents the save state of the currently loaded program on the Universal Robots controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = program_save_state()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		'''Determines whether the specified object is equal to this program save state.'''
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		'''Returns a hash code for this program save state.'''
		return self._instance.GetHashCode()

	@property
	def is_saved(self) -> bool:
		'''Is the program saved'''
		return self._instance.IsSaved

	@is_saved.setter
	def is_saved(self, value: bool):
		self._instance.IsSaved = value

	@property
	def name(self) -> str:
		'''Name of the loaded program'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ProgramSaveState):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
