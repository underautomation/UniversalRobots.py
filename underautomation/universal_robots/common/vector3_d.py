from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Common import Vector3D as vector3_d

class Vector3D:
	'''Represents a three-dimensional vector with X, Y, and Z components.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vector3_d()
		else:
			self._instance = _internal

	@property
	def x(self) -> float:
		'''X component of the vector.'''
		return self._instance.X

	@x.setter
	def x(self, value: float):
		self._instance.X = value

	@property
	def y(self) -> float:
		'''Y component of the vector.'''
		return self._instance.Y

	@y.setter
	def y(self, value: float):
		self._instance.Y = value

	@property
	def z(self) -> float:
		'''Z component of the vector.'''
		return self._instance.Z

	@z.setter
	def z(self, value: float):
		self._instance.Z = value

	@property
	def values(self) -> typing.List[float]:
		'''Underlying array of 3 double values storing X, Y, Z in that order.'''
		return self._instance.Values

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Vector3D):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
