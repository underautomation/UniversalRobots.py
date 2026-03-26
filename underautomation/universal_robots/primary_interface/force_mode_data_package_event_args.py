import typing
from __future__ import annotation
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import ForceModeDataPackageEventArgs as force_mode_data_package_event_args

class ForceModeDataPackageEventArgs(PackageEventArgs):
	'''Force mode data'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = force_mode_data_package_event_args()
		else:
			self._instance = _internal

	@property
	def x(self) -> float:
		'''X force in tool frame in N'''
		return self._instance.X

	@x.setter
	def x(self, value: float):
		self._instance.X = value

	@property
	def y(self) -> float:
		'''Y force in tool frame in N'''
		return self._instance.Y

	@y.setter
	def y(self, value: float):
		self._instance.Y = value

	@property
	def z(self) -> float:
		'''Z force in tool frame in N'''
		return self._instance.Z

	@z.setter
	def z(self, value: float):
		self._instance.Z = value

	@property
	def rx(self) -> float:
		'''Rx torque in tool frame in Nm'''
		return self._instance.Rx

	@rx.setter
	def rx(self, value: float):
		self._instance.Rx = value

	@property
	def ry(self) -> float:
		'''Ry torque in tool frame in Nm'''
		return self._instance.Ry

	@ry.setter
	def ry(self, value: float):
		self._instance.Ry = value

	@property
	def rz(self) -> float:
		'''Rz torque in tool frame in Nm'''
		return self._instance.Rz

	@rz.setter
	def rz(self, value: float):
		self._instance.Rz = value

	@property
	def robot_dexterity(self) -> float:
		'''Dexterity of the robot'''
		return self._instance.RobotDexterity

	@robot_dexterity.setter
	def robot_dexterity(self, value: float):
		self._instance.RobotDexterity = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ForceModeDataPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
