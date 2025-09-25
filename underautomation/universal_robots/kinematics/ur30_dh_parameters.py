import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Kinematics import Ur30DhParameters as ur30_dh_parameters

class Ur30DhParameters:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ur30_dh_parameters()
		else:
			self._instance = _internal
	@property
	def a2(self) -> float:
		return self._instance.A2
	@property
	def a3(self) -> float:
		return self._instance.A3
	@property
	def d1(self) -> float:
		return self._instance.D1
	@property
	def d4(self) -> float:
		return self._instance.D4
	@property
	def d5(self) -> float:
		return self._instance.D5
	@property
	def d6(self) -> float:
		return self._instance.D6
