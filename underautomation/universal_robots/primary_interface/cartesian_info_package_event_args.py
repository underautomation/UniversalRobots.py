import typing
from __future__ import annotation
from underautomation.universal_robots.common.pose import Pose
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import CartesianInfoPackageEventArgs as cartesian_info_package_event_args

class CartesianInfoPackageEventArgs(PackageEventArgs):
	'''Contains current cartesian position of the robot, including its TCP offset'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_info_package_event_args()
		else:
			self._instance = _internal

	def as_pose(self) -> Pose:
		'''Returns the current cartesian position as a Pose object'''
		return Pose(None, None, None, None, None, None, self._instance.AsPose())

	def as_tcp_offset_pose(self) -> Pose:
		'''Returns the TCP offset as a Pose object'''
		return Pose(None, None, None, None, None, None, self._instance.AsTCPOffsetPose())

	@property
	def x(self) -> float:
		'''X axis coordinate in meter of the TCP in the current frame'''
		return self._instance.X

	@x.setter
	def x(self, value: float):
		self._instance.X = value

	@property
	def y(self) -> float:
		'''Y axis coordinate in meter of the TCP in the current frame'''
		return self._instance.Y

	@y.setter
	def y(self, value: float):
		self._instance.Y = value

	@property
	def z(self) -> float:
		'''Z axis coordinate in meter of the TCP in the current frame'''
		return self._instance.Z

	@z.setter
	def z(self, value: float):
		self._instance.Z = value

	@property
	def rx(self) -> float:
		'''RX axis coordinate in rad of the TCP in the current frame'''
		return self._instance.Rx

	@rx.setter
	def rx(self, value: float):
		self._instance.Rx = value

	@property
	def ry(self) -> float:
		'''RY axis coordinate in rad of the TCP in the current frame'''
		return self._instance.Ry

	@ry.setter
	def ry(self, value: float):
		self._instance.Ry = value

	@property
	def rz(self) -> float:
		'''RZ axis coordinate in rad of the TCP in the current frame'''
		return self._instance.Rz

	@rz.setter
	def rz(self, value: float):
		self._instance.Rz = value

	@property
	def tcp_offset_x(self) -> float:
		'''X position of the TCP in the flange frame in meter'''
		return self._instance.TCPOffsetX

	@tcp_offset_x.setter
	def tcp_offset_x(self, value: float):
		self._instance.TCPOffsetX = value

	@property
	def tcp_offset_y(self) -> float:
		'''Y position of the TCP in the flange frame in meter'''
		return self._instance.TCPOffsetY

	@tcp_offset_y.setter
	def tcp_offset_y(self, value: float):
		self._instance.TCPOffsetY = value

	@property
	def tcp_offset_z(self) -> float:
		'''Z position of the TCP in the flange frame in meter'''
		return self._instance.TCPOffsetZ

	@tcp_offset_z.setter
	def tcp_offset_z(self, value: float):
		self._instance.TCPOffsetZ = value

	@property
	def tcp_offset_rx(self) -> float:
		'''RX position of the TCP in the flange frame in rad'''
		return self._instance.TCPOffsetRX

	@tcp_offset_rx.setter
	def tcp_offset_rx(self, value: float):
		self._instance.TCPOffsetRX = value

	@property
	def tcp_offset_ry(self) -> float:
		'''RY position of the TCP in the flange frame in rad'''
		return self._instance.TCPOffsetRY

	@tcp_offset_ry.setter
	def tcp_offset_ry(self, value: float):
		self._instance.TCPOffsetRY = value

	@property
	def tcp_offset_rz(self) -> float:
		'''RZ position of the TCP in the flange frame in rad'''
		return self._instance.TCPOffsetRZ

	@tcp_offset_rz.setter
	def tcp_offset_rz(self, value: float):
		self._instance.TCPOffsetRZ = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianInfoPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
