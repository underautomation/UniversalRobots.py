from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Common import CartesianCoordinates as cartesian_coordinates

class CartesianCoordinates:
	'''Represents a cartesian pose with 3 translations and 3 rotations'''
	def __init__(self, x: float, y: float, z: float, rx: float, ry: float, rz: float, _internal = 0):
		'''Creates a new pose with translations and rotations information'''
		if(_internal == 0):
			self._instance = cartesian_coordinates(x, y, z, rx, ry, rz)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		'''Determines whether the specified object is equal to the current cartesian coordinates.

		:param obj: The object to compare with.
		:returns: true if coordinates are equal; otherwise, false.
		'''
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		'''Returns a hash code for this cartesian coordinates instance.

		:returns: A hash code based on all six coordinate values.
		'''
		return self._instance.GetHashCode()

	@property
	def x(self) -> float:
		'''X coordinate in meters or m/s'''
		return self._instance.X

	@x.setter
	def x(self, value: float):
		self._instance.X = value

	@property
	def y(self) -> float:
		'''Y coordinate in meters or m/s'''
		return self._instance.Y

	@y.setter
	def y(self, value: float):
		self._instance.Y = value

	@property
	def z(self) -> float:
		'''Z coordinate in meters or m/s'''
		return self._instance.Z

	@z.setter
	def z(self, value: float):
		self._instance.Z = value

	@property
	def rx(self) -> float:
		'''RX rotation in radians or radians/s'''
		return self._instance.Rx

	@rx.setter
	def rx(self, value: float):
		self._instance.Rx = value

	@property
	def ry(self) -> float:
		'''RY rotation in radians or radians/s'''
		return self._instance.Ry

	@ry.setter
	def ry(self, value: float):
		self._instance.Ry = value

	@property
	def rz(self) -> float:
		'''RZ rotation in radians or radians/s'''
		return self._instance.Rz

	@rz.setter
	def rz(self, value: float):
		self._instance.Rz = value

	@property
	def values(self) -> typing.List[float]:
		'''Underlying array of 6 double values storing X, Y, Z, Rx, Ry, Rz in that order.'''
		return self._instance.Values

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianCoordinates):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
