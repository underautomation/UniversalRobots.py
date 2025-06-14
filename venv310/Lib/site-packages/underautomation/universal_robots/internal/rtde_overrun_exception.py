import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Internal import RtdeOverrunException as rtde_overrun_exception

class RtdeOverrunException:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_overrun_exception()
		else:
			self._instance = _internal
