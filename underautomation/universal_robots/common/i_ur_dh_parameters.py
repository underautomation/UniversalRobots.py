from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Common import IUrDhParameters as i_ur_dh_parameters

class IUrDhParameters:
	'''Denavit–Hartenberg (DH) parameters for Universal Robots with only the relevant parameters'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_ur_dh_parameters()
		else:
			self._instance = _internal

	@property
	def a2(self) -> float:
		'''DH parameter a2 (Shoulder)'''
		return self._instance.A2

	@property
	def a3(self) -> float:
		'''DH parameter a3 (Elbow)'''
		return self._instance.A3

	@property
	def d1(self) -> float:
		'''DH parameter d1 (Base)'''
		return self._instance.D1

	@property
	def d4(self) -> float:
		'''DH parameter d4 (Wrist1)'''
		return self._instance.D4

	@property
	def d5(self) -> float:
		'''DH parameter d5 (Wrist2)'''
		return self._instance.D5

	@property
	def d6(self) -> float:
		'''DH parameter d6 (Wrist3/Tool)'''
		return self._instance.D6

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IUrDhParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
