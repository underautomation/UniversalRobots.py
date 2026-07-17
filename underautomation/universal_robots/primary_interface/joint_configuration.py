from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.PrimaryInterface import JointConfiguration as joint_configuration

class JointConfiguration:
	'''Joint configuration'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_configuration()
		else:
			self._instance = _internal

	@property
	def joint_min_limit(self) -> float:
		'''Minimum angular position in rad'''
		return self._instance.JointMinLimit

	@joint_min_limit.setter
	def joint_min_limit(self, value: float):
		self._instance.JointMinLimit = value

	@property
	def joint_max_limit(self) -> float:
		'''Maximum angular position in rad'''
		return self._instance.JointMaxLimit

	@joint_max_limit.setter
	def joint_max_limit(self, value: float):
		self._instance.JointMaxLimit = value

	@property
	def joint_max_speed(self) -> float:
		'''Maximum rotation speed in rad/s'''
		return self._instance.JointMaxSpeed

	@joint_max_speed.setter
	def joint_max_speed(self, value: float):
		self._instance.JointMaxSpeed = value

	@property
	def joint_max_acceleration(self) -> float:
		'''Maximum rotation speed in rad/s²'''
		return self._instance.JointMaxAcceleration

	@joint_max_acceleration.setter
	def joint_max_acceleration(self, value: float):
		self._instance.JointMaxAcceleration = value

	@property
	def d_ha(self) -> float:
		'''a parameter of Denavit–Hartenberg (DH) convention'''
		return self._instance.DHa

	@d_ha.setter
	def d_ha(self, value: float):
		self._instance.DHa = value

	@property
	def d_hd(self) -> float:
		'''d parameter of Denavit–Hartenberg (DH) convention'''
		return self._instance.DHd

	@d_hd.setter
	def d_hd(self, value: float):
		self._instance.DHd = value

	@property
	def d_halpha(self) -> float:
		'''Alpha parameter of Denavit–Hartenberg (DH) convention'''
		return self._instance.DHalpha

	@d_halpha.setter
	def d_halpha(self, value: float):
		self._instance.DHalpha = value

	@property
	def d_htheta(self) -> float:
		'''Theta parameter of Denavit–Hartenberg (DH) convention'''
		return self._instance.DHtheta

	@d_htheta.setter
	def d_htheta(self, value: float):
		self._instance.DHtheta = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointConfiguration):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
