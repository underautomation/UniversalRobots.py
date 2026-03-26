import typing
from __future__ import annotation
from underautomation.universal_robots.common.i_ur_dh_parameters import IUrDhParameters
from underautomation.universal_robots.primary_interface.joint_kinematics_info import JointKinematicsInfo
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import KinematicsInfoPackageEventArgs as kinematics_info_package_event_args

class KinematicsInfoPackageEventArgs(PackageEventArgs, IUrDhParameters):
	'''Kinematics info'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kinematics_info_package_event_args()
		else:
			self._instance = _internal

	@property
	def calibration_status(self) -> int:
		'''Calibration status (0 : OK)'''
		return self._instance.CalibrationStatus

	@calibration_status.setter
	def calibration_status(self, value: int):
		self._instance.CalibrationStatus = value

	@property
	def base(self) -> JointKinematicsInfo:
		'''Base kinematics info'''
		return JointKinematicsInfo(self._instance.Base)

	@base.setter
	def base(self, value: JointKinematicsInfo):
		self._instance.Base = value._instance if value else None

	@property
	def shoulder(self) -> JointKinematicsInfo:
		'''Shoulder kinematics info'''
		return JointKinematicsInfo(self._instance.Shoulder)

	@shoulder.setter
	def shoulder(self, value: JointKinematicsInfo):
		self._instance.Shoulder = value._instance if value else None

	@property
	def elbow(self) -> JointKinematicsInfo:
		'''Elbow kinematics info'''
		return JointKinematicsInfo(self._instance.Elbow)

	@elbow.setter
	def elbow(self, value: JointKinematicsInfo):
		self._instance.Elbow = value._instance if value else None

	@property
	def wrist1(self) -> JointKinematicsInfo:
		'''Wrist1 kinematics info'''
		return JointKinematicsInfo(self._instance.Wrist1)

	@wrist1.setter
	def wrist1(self, value: JointKinematicsInfo):
		self._instance.Wrist1 = value._instance if value else None

	@property
	def wrist2(self) -> JointKinematicsInfo:
		'''Wrist2 kinematics info'''
		return JointKinematicsInfo(self._instance.Wrist2)

	@wrist2.setter
	def wrist2(self, value: JointKinematicsInfo):
		self._instance.Wrist2 = value._instance if value else None

	@property
	def wrist3(self) -> JointKinematicsInfo:
		'''Wrist3 (Tool) kinematics info'''
		return JointKinematicsInfo(self._instance.Wrist3)

	@wrist3.setter
	def wrist3(self, value: JointKinematicsInfo):
		self._instance.Wrist3 = value._instance if value else None

	@property
	def a2(self) -> float:
		'''DH parameter a2 (Shoulder.DHa)'''
		return self._instance.A2

	@property
	def a3(self) -> float:
		'''DH parameter a3 (Elbow.DHa)'''
		return self._instance.A3

	@property
	def d1(self) -> float:
		'''DH parameter d1 (Base.DHd)'''
		return self._instance.D1

	@property
	def d4(self) -> float:
		'''DH parameter d4 (Wrist1.DHd)'''
		return self._instance.D4

	@property
	def d5(self) -> float:
		'''DH parameter d5 (Wrist2.DHd)'''
		return self._instance.D5

	@property
	def d6(self) -> float:
		'''DH parameter d6 (Wrist3.DHd)'''
		return self._instance.D6

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, KinematicsInfoPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
