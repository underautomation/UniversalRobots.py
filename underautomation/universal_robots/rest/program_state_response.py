from __future__ import annotations
import typing
from underautomation.universal_robots.rest.rest_program_state import RestProgramState
from UnderAutomation.UniversalRobots.Rest import ProgramStateResponse as program_state_response
from UnderAutomation.UniversalRobots.Rest import RestProgramState as rest_program_state

class ProgramStateResponse:
	'''Response from GET /program/v1/state endpoint'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = program_state_response()
		else:
			self._instance = _internal

	@property
	def state(self) -> RestProgramState:
		'''Current state of the program'''
		return RestProgramState(int(self._instance.State))

	@state.setter
	def state(self, value: RestProgramState):
		self._instance.State = rest_program_state(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ProgramStateResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
