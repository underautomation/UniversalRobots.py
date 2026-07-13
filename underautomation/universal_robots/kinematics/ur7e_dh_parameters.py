from __future__ import annotations
import typing
from underautomation.universal_robots.kinematics.ur5e_dh_parameters import Ur5eDhParameters
from UnderAutomation.UniversalRobots.Kinematics import Ur7eDhParameters as ur7e_dh_parameters

class Ur7eDhParameters(Ur5eDhParameters):
	'''Denavit-Hartenberg parameters for the UR7e robot (e-Series). Shares the same DH values as the UR5e.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ur7e_dh_parameters()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Ur7eDhParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
