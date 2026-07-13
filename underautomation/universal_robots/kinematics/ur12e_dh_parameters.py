from __future__ import annotations
import typing
from underautomation.universal_robots.kinematics.ur10e_dh_parameters import Ur10eDhParameters
from UnderAutomation.UniversalRobots.Kinematics import Ur12eDhParameters as ur12e_dh_parameters

class Ur12eDhParameters(Ur10eDhParameters):
	'''Denavit-Hartenberg parameters for the UR12e robot (e-Series). Shares the same DH values as the UR10e.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ur12e_dh_parameters()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Ur12eDhParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
