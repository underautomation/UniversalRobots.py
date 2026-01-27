import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rest import ProgramStateAction as program_state_action

class ProgramStateAction(int):
	play = program_state_action.play
	pause = program_state_action.pause
	stop = program_state_action.stop
	resume = program_state_action.resume
