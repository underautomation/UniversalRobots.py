import typing
from __future__ import annotation
from underautomation.universal_robots.primary_interface.joint_data import JointData
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import JointDataPackageEventArgs as joint_data_package_event_args

class JointDataPackageEventArgs(PackageEventArgs):
	'''Status of each joints'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_data_package_event_args()
		else:
			self._instance = _internal

	@property
	def base(self) -> JointData:
		'''Base joint data'''
		return JointData(self._instance.Base)

	@base.setter
	def base(self, value: JointData):
		self._instance.Base = value._instance if value else None

	@property
	def shoulder(self) -> JointData:
		'''Shoulder joint data'''
		return JointData(self._instance.Shoulder)

	@shoulder.setter
	def shoulder(self, value: JointData):
		self._instance.Shoulder = value._instance if value else None

	@property
	def elbow(self) -> JointData:
		'''Elbow joint data'''
		return JointData(self._instance.Elbow)

	@elbow.setter
	def elbow(self, value: JointData):
		self._instance.Elbow = value._instance if value else None

	@property
	def wrist1(self) -> JointData:
		'''Wrist1 joint data'''
		return JointData(self._instance.Wrist1)

	@wrist1.setter
	def wrist1(self, value: JointData):
		self._instance.Wrist1 = value._instance if value else None

	@property
	def wrist2(self) -> JointData:
		'''Wrist2 joint data'''
		return JointData(self._instance.Wrist2)

	@wrist2.setter
	def wrist2(self, value: JointData):
		self._instance.Wrist2 = value._instance if value else None

	@property
	def wrist3(self) -> JointData:
		'''Wrist3 (Tool) joint data'''
		return JointData(self._instance.Wrist3)

	@wrist3.setter
	def wrist3(self, value: JointData):
		self._instance.Wrist3 = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointDataPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
