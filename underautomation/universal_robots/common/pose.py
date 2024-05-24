import typing
from underautomation.universal_robots.common.cartesian_coordinates import CartesianCoordinates
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import Pose as pose

class Pose(CartesianCoordinates):
	def __init__(self, x: float, y: float, z: float, rx: float, ry: float, rz: float, _internal = 0):
		if(_internal == 0):
			self._instance = pose(x, y, z, rx, ry, rz)
		else:
			self._instance = _internal
	def from_rotation_vector_to_rpy(self) -> 'Pose':
		return Pose(None, None, None, None, None, None, self._instance.FromRotationVectorToRPY())
	def from_rpy_to_rotation_vector(self) -> 'Pose':
		return Pose(None, None, None, None, None, None, self._instance.FromRPYToRotationVector())
	def __repr__(self):
		return self._instance.ToString()
	@staticmethod
	def try_parse(value: str, pose: 'Pose') -> bool:
		return pose.TryParse(value, pose._instance)
	def from_rotation_vector_to_quaternion(self, x: float, y: float, z: float, w: float) -> None:
		self._instance.FromRotationVectorToQuaternion(x, y, z, w)
	@staticmethod
	def from_quaternion_to_rotation_vector(x: float, y: float, z: float, w: float) -> 'Pose':
		return Pose(None, None, None, None, None, None, pose.FromQuaternionToRotationVector(x, y, z, w))
	@property
	def rx_degrees(self) -> float:
		return self._instance.RxDegrees
	@rx_degrees.setter
	def rx_degrees(self, value: float):
		self._instance.RxDegrees = value
	@property
	def ry_degrees(self) -> float:
		return self._instance.RyDegrees
	@ry_degrees.setter
	def ry_degrees(self, value: float):
		self._instance.RyDegrees = value
	@property
	def rz_degrees(self) -> float:
		return self._instance.RzDegrees
	@rz_degrees.setter
	def rz_degrees(self, value: float):
		self._instance.RzDegrees = value
