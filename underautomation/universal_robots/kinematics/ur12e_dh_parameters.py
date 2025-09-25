import typing
from underautomation.universal_robots.kinematics.ur10e_dh_parameters import Ur10eDhParameters
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Kinematics import Ur12eDhParameters as ur12e_dh_parameters

class Ur12eDhParameters(Ur10eDhParameters):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ur12e_dh_parameters()
		else:
			self._instance = _internal
