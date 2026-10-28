from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Rest import RestProgramInfo as rest_program_info

class RestProgramInfo:
	'''Description of a program stored on a PolyScope X robot, returned by get_programs().'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rest_program_info()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the program.'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def description(self) -> str:
		'''Description of the program. Empty if the robot gives none.'''
		return self._instance.Description

	@description.setter
	def description(self, value: str):
		self._instance.Description = value

	@property
	def program_state(self) -> str:
		'''State of the program as text. Empty if the robot gives none.'''
		return self._instance.ProgramState

	@program_state.setter
	def program_state(self, value: str):
		self._instance.ProgramState = value

	@property
	def created_date(self) -> int:
		'''Creation date, in milliseconds since 1970-01-01 UTC. 0 if the robot gives none.'''
		return self._instance.CreatedDate

	@created_date.setter
	def created_date(self, value: int):
		self._instance.CreatedDate = value

	@property
	def last_modified_date(self) -> int:
		'''Date of the last modification, in milliseconds since 1970-01-01 UTC. 0 if the robot gives none.'''
		return self._instance.LastModifiedDate

	@last_modified_date.setter
	def last_modified_date(self, value: int):
		self._instance.LastModifiedDate = value

	@property
	def last_saved_date(self) -> int:
		'''Date of the last save, in milliseconds since 1970-01-01 UTC. 0 if the robot gives none.'''
		return self._instance.LastSavedDate

	@last_saved_date.setter
	def last_saved_date(self, value: int):
		self._instance.LastSavedDate = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RestProgramInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
