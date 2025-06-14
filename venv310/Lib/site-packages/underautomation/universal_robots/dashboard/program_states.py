import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Dashboard import ProgramStates as program_states

class ProgramStates(int):
	Stopped = program_states.Stopped
	Playing = program_states.Playing
	Paused = program_states.Paused
