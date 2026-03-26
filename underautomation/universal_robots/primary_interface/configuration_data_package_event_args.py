import typing
from __future__ import annotation
from underautomation.universal_robots.common.i_ur_dh_parameters import IUrDhParameters
from underautomation.universal_robots.common.controller_box_types import ControllerBoxTypes
from underautomation.universal_robots.common.robot_models import RobotModels
from underautomation.universal_robots.common.robot_sub_types import RobotSubTypes
from underautomation.universal_robots.primary_interface.joint_configuration import JointConfiguration
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import ConfigurationDataPackageEventArgs as configuration_data_package_event_args
from UnderAutomation.UniversalRobots.Common import ControllerBoxTypes as controller_box_types
from UnderAutomation.UniversalRobots.Common import RobotModels as robot_models
from UnderAutomation.UniversalRobots.Common import RobotSubTypes as robot_sub_types

class ConfigurationDataPackageEventArgs(PackageEventArgs, IUrDhParameters):
	'''Joint configuration'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = configuration_data_package_event_args()
		else:
			self._instance = _internal

	@property
	def v_joint_default(self) -> float:
		'''Default joint angular speed in rad/s'''
		return self._instance.VJointDefault

	@v_joint_default.setter
	def v_joint_default(self, value: float):
		self._instance.VJointDefault = value

	@property
	def a_joint_default(self) -> float:
		'''Default joint acceleration speed in rad/s²'''
		return self._instance.AJointDefault

	@a_joint_default.setter
	def a_joint_default(self, value: float):
		self._instance.AJointDefault = value

	@property
	def v_tool_default(self) -> float:
		'''Default TCP speed speed in m/s'''
		return self._instance.VToolDefault

	@v_tool_default.setter
	def v_tool_default(self, value: float):
		self._instance.VToolDefault = value

	@property
	def a_tool_default(self) -> float:
		'''Default TCP acceleration speed in m/s²'''
		return self._instance.AToolDefault

	@a_tool_default.setter
	def a_tool_default(self, value: float):
		self._instance.AToolDefault = value

	@property
	def eq_radius(self) -> float:
		'''Equipment radius in meter'''
		return self._instance.EqRadius

	@eq_radius.setter
	def eq_radius(self, value: float):
		self._instance.EqRadius = value

	@property
	def masterboard_version(self) -> int:
		'''Masterboard version'''
		return self._instance.MasterboardVersion

	@masterboard_version.setter
	def masterboard_version(self, value: int):
		self._instance.MasterboardVersion = value

	@property
	def controller_box_type(self) -> ControllerBoxTypes:
		'''Controller box type'''
		return ControllerBoxTypes(int(self._instance.ControllerBoxType))

	@controller_box_type.setter
	def controller_box_type(self, value: ControllerBoxTypes):
		self._instance.ControllerBoxType = controller_box_types(int(value))

	@property
	def robot_type(self) -> RobotModels:
		'''Model of the robot (UR3, UR5, UR10, UR16)'''
		return RobotModels(int(self._instance.RobotType))

	@robot_type.setter
	def robot_type(self, value: RobotModels):
		self._instance.RobotType = robot_models(int(value))

	@property
	def robot_sub_type(self) -> RobotSubTypes:
		'''Robot series (e-Series, CB-Series, etc.)'''
		return RobotSubTypes(int(self._instance.RobotSubType))

	@robot_sub_type.setter
	def robot_sub_type(self, value: RobotSubTypes):
		self._instance.RobotSubType = robot_sub_types(int(value))

	@property
	def base(self) -> JointConfiguration:
		'''Base joint configuration'''
		return JointConfiguration(self._instance.Base)

	@base.setter
	def base(self, value: JointConfiguration):
		self._instance.Base = value._instance if value else None

	@property
	def shoulder(self) -> JointConfiguration:
		'''Shoulder joint configuration'''
		return JointConfiguration(self._instance.Shoulder)

	@shoulder.setter
	def shoulder(self, value: JointConfiguration):
		self._instance.Shoulder = value._instance if value else None

	@property
	def elbow(self) -> JointConfiguration:
		'''Elbow joint configuration'''
		return JointConfiguration(self._instance.Elbow)

	@elbow.setter
	def elbow(self, value: JointConfiguration):
		self._instance.Elbow = value._instance if value else None

	@property
	def wrist1(self) -> JointConfiguration:
		'''Wrist1 joint configuration'''
		return JointConfiguration(self._instance.Wrist1)

	@wrist1.setter
	def wrist1(self, value: JointConfiguration):
		self._instance.Wrist1 = value._instance if value else None

	@property
	def wrist2(self) -> JointConfiguration:
		'''Wrist2 joint configuration'''
		return JointConfiguration(self._instance.Wrist2)

	@wrist2.setter
	def wrist2(self, value: JointConfiguration):
		self._instance.Wrist2 = value._instance if value else None

	@property
	def wrist3(self) -> JointConfiguration:
		'''Wrist3 (Tool) joint configuration'''
		return JointConfiguration(self._instance.Wrist3)

	@wrist3.setter
	def wrist3(self, value: JointConfiguration):
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
		if not isinstance(other, ConfigurationDataPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
