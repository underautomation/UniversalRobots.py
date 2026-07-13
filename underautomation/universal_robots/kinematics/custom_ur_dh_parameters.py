from __future__ import annotations
import typing
from underautomation.universal_robots.common.i_ur_dh_parameters import IUrDhParameters
from UnderAutomation.UniversalRobots.Kinematics import CustomUrDhParameters as custom_ur_dh_parameters

class CustomUrDhParameters(IUrDhParameters):
	'''Mutable Denavit-Hartenberg parameters for a Universal Robots arm, allowing custom DH values.'''
	def __init__(self, a2: float, a3: float, d1: float, d4: float, d5: float, d6: float, _internal = 0):
		'''Creates a new instance with the specified DH parameters.

		:param a2: DH parameter a2 (shoulder link length) in meters.
		:param a3: DH parameter a3 (elbow link length) in meters.
		:param d1: DH parameter d1 (base height offset) in meters.
		:param d4: DH parameter d4 (wrist 1 offset) in meters.
		:param d5: DH parameter d5 (wrist 2 offset) in meters.
		:param d6: DH parameter d6 (wrist 3 / tool offset) in meters.
		'''
		if(_internal == 0):
			self._instance = custom_ur_dh_parameters(a2, a3, d1, d4, d5, d6)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def a2(self) -> float:
		'''DH parameter a2 (shoulder link length) in meters.'''
		return self._instance.A2

	@a2.setter
	def a2(self, value: float):
		self._instance.A2 = value

	@property
	def a3(self) -> float:
		'''DH parameter a3 (elbow link length) in meters.'''
		return self._instance.A3

	@a3.setter
	def a3(self, value: float):
		self._instance.A3 = value

	@property
	def d1(self) -> float:
		'''DH parameter d1 (base height offset) in meters.'''
		return self._instance.D1

	@d1.setter
	def d1(self, value: float):
		self._instance.D1 = value

	@property
	def d4(self) -> float:
		'''DH parameter d4 (wrist 1 offset) in meters.'''
		return self._instance.D4

	@d4.setter
	def d4(self, value: float):
		self._instance.D4 = value

	@property
	def d5(self) -> float:
		'''DH parameter d5 (wrist 2 offset) in meters.'''
		return self._instance.D5

	@d5.setter
	def d5(self, value: float):
		self._instance.D5 = value

	@property
	def d6(self) -> float:
		'''DH parameter d6 (wrist 3 / tool offset) in meters.'''
		return self._instance.D6

	@d6.setter
	def d6(self, value: float):
		self._instance.D6 = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CustomUrDhParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
