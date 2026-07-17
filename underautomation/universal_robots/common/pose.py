from __future__ import annotations
import typing
from underautomation.universal_robots.common.cartesian_coordinates import CartesianCoordinates
from UnderAutomation.UniversalRobots.Common import Pose as pose

class Pose(CartesianCoordinates):
	'''Represents a UR pose'''
	def __init__(self, x: float, y: float, z: float, rx: float, ry: float, rz: float, _internal = 0):
		'''Creates a new pose with the specified translation and rotation.

		:param x: X translation in meters.
		:param y: Y translation in meters.
		:param z: Z translation in meters.
		:param rx: Rotation vector X component in radians.
		:param ry: Rotation vector Y component in radians.
		:param rz: Rotation vector Z component in radians.
		'''
		if(_internal == 0):
			self._instance = pose(x, y, z, rx, ry, rz)
		else:
			self._instance = _internal

	def from_rotation_vector_to_rpy(self) -> 'Pose':
		'''Consider this pose as a Rotation Vector And convert it to a new RPY position'''
		return Pose(None, None, None, None, None, None, self._instance.FromRotationVectorToRPY())

	def from_rpy_to_rotation_vector(self) -> 'Pose':
		'''Consider this pose as RPY And convert it to a new Rotation Vector'''
		return Pose(None, None, None, None, None, None, self._instance.FromRPYToRotationVector())

	@staticmethod
	def try_parse(value: str, pose: 'Pose') -> bool:
		'''Parse a pose from its string representation

		:param value: String representation of the pose like : p[0.1,0,0.2,0.01,0,0]
		:param pose: The output parsed pose
		'''
		return pose.TryParse(value, pose._instance if pose else None)

	def from_rotation_vector_to_quaternion(self, x: float, y: float, z: float, w: float) -> None:
		'''Converts a rotation vector to quaternion'''
		self._instance.FromRotationVectorToQuaternion(x, y, z, w)

	def from_rpy_to4x4_matrix(self) -> typing.List[float]:
		'''Consider this pose as a RPY (Roll-Pitch-Yaw) representation and return a 4x4 homogeneous transformation matrix.

		:returns: A 4x4 double array representing the transformation matrix.
		'''
		return self._instance.FromRPYTo4x4Matrix()

	def from_rotation_vector_to4x4_matrix(self) -> typing.List[float]:
		'''Consider this pose as a rotation vector and return a 4x4 homogeneous transformation matrix.

		:returns: A 4x4 double array representing the transformation matrix.
		'''
		return self._instance.FromRotationVectorTo4x4Matrix()

	@staticmethod
	def from_quaternion_to_rotation_vector(x: float, y: float, z: float, w: float) -> 'Pose':
		'''Converts a quaternion to UR rotation vector'''
		return Pose(None, None, None, None, None, None, pose.FromQuaternionToRotationVector(x, y, z, w))

	@staticmethod
	def from4x4_matrix_to_rotation_vector(matrixTransform: typing.List[float]) -> 'Pose':
		return Pose(None, None, None, None, None, None, pose.From4x4MatrixToRotationVector(matrixTransform))

	@staticmethod
	def from4x4_matrix_to_rpy(matrixTransform: typing.List[float]) -> 'Pose':
		return Pose(None, None, None, None, None, None, pose.From4x4MatrixToRPY(matrixTransform))

	@property
	def rx_degrees(self) -> float:
		'''RX rotation in degrees or °/s'''
		return self._instance.RxDegrees

	@rx_degrees.setter
	def rx_degrees(self, value: float):
		self._instance.RxDegrees = value

	@property
	def ry_degrees(self) -> float:
		'''RY rotation in degrees or °/s'''
		return self._instance.RyDegrees

	@ry_degrees.setter
	def ry_degrees(self, value: float):
		self._instance.RyDegrees = value

	@property
	def rz_degrees(self) -> float:
		'''RZ rotation in degrees or °/s'''
		return self._instance.RzDegrees

	@rz_degrees.setter
	def rz_degrees(self, value: float):
		self._instance.RzDegrees = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Pose):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
