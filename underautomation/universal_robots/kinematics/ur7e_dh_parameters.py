import typing
from underautomation.universal_robots.kinematics.ur5e_dh_parameters import Ur5eDhParameters
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Kinematics import Ur7eDhParameters as ur7e_dh_parameters

class Ur7eDhParameters(Ur5eDhParameters):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ur7e_dh_parameters()
		else:
			self._instance = _internal
