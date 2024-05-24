import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rtde import RTDEStates as rtde_states

class RTDEStates(int):
	Disabled = rtde_states.Disabled
	Connecting = rtde_states.Connecting
	Started = rtde_states.Started
	Paused = rtde_states.Paused
