import typing
from underautomation.universal_robots.rest.rest_program_state import RestProgramState
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rest import ProgramStateResponse as program_state_response

class ProgramStateResponse:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = program_state_response()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def state(self) -> RestProgramState:
		return RestProgramState(self._instance.State)
	@state.setter
	def state(self, value: RestProgramState):
		self._instance.State = value
