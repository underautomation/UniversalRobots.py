from __future__ import annotations
import typing
from underautomation.universal_robots.common.i_ur_dh_parameters import IUrDhParameters
from UnderAutomation.UniversalRobots.Kinematics import Ur10DhParameters as ur10_dh_parameters

class Ur10DhParameters(IUrDhParameters):
	'''Denavit-Hartenberg parameters for the UR10 robot (CB-Series).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ur10_dh_parameters()
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

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Ur10DhParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
