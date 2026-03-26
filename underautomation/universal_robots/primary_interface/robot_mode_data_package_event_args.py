import typing
from __future__ import annotation
from underautomation.universal_robots.common.robot_modes import RobotModes
from underautomation.universal_robots.common.control_modes import ControlModes
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import RobotModeDataPackageEventArgs as robot_mode_data_package_event_args
from UnderAutomation.UniversalRobots.Common import RobotModes as robot_modes
from UnderAutomation.UniversalRobots.Common import ControlModes as control_modes

class RobotModeDataPackageEventArgs(PackageEventArgs):
	'''Information about current robot mode'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_mode_data_package_event_args()
		else:
			self._instance = _internal

	@property
	def timestamp(self) -> typing.Any:
		'''Timespan since the robot controller has started'''
		return self._instance.Timestamp

	@timestamp.setter
	def timestamp(self, value: typing.Any):
		self._instance.Timestamp = value

	@property
	def physical_robot_connected(self) -> bool:
		'''Robot is connected to its controller'''
		return self._instance.PhysicalRobotConnected

	@physical_robot_connected.setter
	def physical_robot_connected(self, value: bool):
		self._instance.PhysicalRobotConnected = value

	@property
	def real_robot_enabled(self) -> bool:
		'''Real robot mode active. False if robot is in simulation'''
		return self._instance.RealRobotEnabled

	@real_robot_enabled.setter
	def real_robot_enabled(self, value: bool):
		self._instance.RealRobotEnabled = value

	@property
	def robot_power_on(self) -> bool:
		'''Robot is powered on and boot is completed. If false, you need to press "ON" button to power it on'''
		return self._instance.RobotPowerOn

	@robot_power_on.setter
	def robot_power_on(self, value: bool):
		self._instance.RobotPowerOn = value

	@property
	def emergency_stopped(self) -> bool:
		'''The button Emergency Stop is pressed'''
		return self._instance.EmergencyStopped

	@emergency_stopped.setter
	def emergency_stopped(self, value: bool):
		self._instance.EmergencyStopped = value

	@property
	def protective_stopped(self) -> bool:
		'''A stop occured due to a fault detection'''
		return self._instance.ProtectiveStopped

	@protective_stopped.setter
	def protective_stopped(self, value: bool):
		self._instance.ProtectiveStopped = value

	@property
	def program_running(self) -> bool:
		'''A program is running'''
		return self._instance.ProgramRunning

	@program_running.setter
	def program_running(self, value: bool):
		self._instance.ProgramRunning = value

	@property
	def program_paused(self) -> bool:
		'''The running program is paused'''
		return self._instance.ProgramPaused

	@program_paused.setter
	def program_paused(self, value: bool):
		self._instance.ProgramPaused = value

	@property
	def robot_mode(self) -> RobotModes:
		'''Current robot running mode'''
		return RobotModes(int(self._instance.RobotMode))

	@robot_mode.setter
	def robot_mode(self, value: RobotModes):
		self._instance.RobotMode = robot_modes(int(value))

	@property
	def control_mode(self) -> ControlModes:
		'''Current robot control mode'''
		return ControlModes(int(self._instance.ControlMode))

	@control_mode.setter
	def control_mode(self, value: ControlModes):
		self._instance.ControlMode = control_modes(int(value))

	@property
	def target_speed_fraction(self) -> float:
		'''Overriden speed ratio between 0 (0%) and 1 (100%)'''
		return self._instance.TargetSpeedFraction

	@target_speed_fraction.setter
	def target_speed_fraction(self, value: float):
		self._instance.TargetSpeedFraction = value

	@property
	def speed_scaling(self) -> float:
		'''Speed scaling'''
		return self._instance.SpeedScaling

	@speed_scaling.setter
	def speed_scaling(self, value: float):
		self._instance.SpeedScaling = value

	@property
	def target_speed_fraction_limit(self) -> float:
		'''Maximum target speed fraction'''
		return self._instance.TargetSpeedFractionLimit

	@target_speed_fraction_limit.setter
	def target_speed_fraction_limit(self, value: float):
		self._instance.TargetSpeedFractionLimit = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotModeDataPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
