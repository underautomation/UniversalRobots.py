import typing
from underautomation.universal_robots.common.i_ur_dh_parameters import IUrDhParameters
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Kinematics import CustomUrDhParameters as custom_ur_dh_parameters

class CustomUrDhParameters:
	def __init__(self, a2: float, a3: float, d1: float, d4: float, d5: float, d6: float, _internal = 0):
		if(_internal == 0):
			self._instance = custom_ur_dh_parameters(a2, a3, d1, d4, d5, d6)
		else:
			self._instance = _internal
	@property
	def a2(self) -> float:
		return self._instance.A2
	@a2.setter
	def a2(self, value: float):
		self._instance.A2 = value
	@property
	def a3(self) -> float:
		return self._instance.A3
	@a3.setter
	def a3(self, value: float):
		self._instance.A3 = value
	@property
	def d1(self) -> float:
		return self._instance.D1
	@d1.setter
	def d1(self, value: float):
		self._instance.D1 = value
	@property
	def d4(self) -> float:
		return self._instance.D4
	@d4.setter
	def d4(self, value: float):
		self._instance.D4 = value
	@property
	def d5(self) -> float:
		return self._instance.D5
	@d5.setter
	def d5(self, value: float):
		self._instance.D5 = value
	@property
	def d6(self) -> float:
		return self._instance.D6
	@d6.setter
	def d6(self, value: float):
		self._instance.D6 = value
