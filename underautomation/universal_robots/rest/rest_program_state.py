import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rest import RestProgramState as rest_program_state

class RestProgramState(int):
	Unknown = rest_program_state.Unknown
	Stopped = rest_program_state.Stopped
	Playing = rest_program_state.Playing
	Paused = rest_program_state.Paused
