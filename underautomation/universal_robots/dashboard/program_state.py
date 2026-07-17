from __future__ import annotations
import typing
from underautomation.universal_robots.dashboard.program_states import ProgramStates
from UnderAutomation.UniversalRobots.Dashboard import ProgramState as program_state
from UnderAutomation.UniversalRobots.Dashboard import ProgramStates as program_states

class ProgramState:
	'''Describes a program state (its running state and its name)'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = program_state()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		'''Determines whether the specified object is equal to this program state.'''
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		'''Returns a hash code for this program state.'''
		return self._instance.GetHashCode()

	@property
	def state(self) -> ProgramStates:
		'''Running state of the loaded program'''
		return ProgramStates(int(self._instance.State))

	@state.setter
	def state(self, value: ProgramStates):
		self._instance.State = program_states(int(value))

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
		if not isinstance(other, ProgramState):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
