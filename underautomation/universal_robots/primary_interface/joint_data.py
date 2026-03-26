import typing
from __future__ import annotation
from underautomation.universal_robots.common.joint_modes import JointModes
from UnderAutomation.UniversalRobots.PrimaryInterface import JointData as joint_data
from UnderAutomation.UniversalRobots.Common import JointModes as joint_modes

class JointData:
	'''Joint data'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_data()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def position(self) -> float:
		'''Angular joint position in radian'''
		return self._instance.Position

	@position.setter
	def position(self, value: float):
		self._instance.Position = value

	@property
	def target_position(self) -> float:
		'''Angular target position in radian'''
		return self._instance.TargetPosition

	@target_position.setter
	def target_position(self, value: float):
		self._instance.TargetPosition = value

	@property
	def actual_speed(self) -> float:
		'''Joint rotation speed in rad/s'''
		return self._instance.ActualSpeed

	@actual_speed.setter
	def actual_speed(self, value: float):
		self._instance.ActualSpeed = value

	@property
	def current(self) -> float:
		'''Motor current in Amps'''
		return self._instance.Current

	@current.setter
	def current(self, value: float):
		self._instance.Current = value

	@property
	def voltage(self) -> float:
		'''Motor voltage in Volts'''
		return self._instance.Voltage

	@voltage.setter
	def voltage(self, value: float):
		self._instance.Voltage = value

	@property
	def temperature(self) -> float:
		'''Joint temperature in °C'''
		return self._instance.Temperature

	@temperature.setter
	def temperature(self, value: float):
		self._instance.Temperature = value

	@property
	def joint_mode(self) -> JointModes:
		'''Joint mode'''
		return JointModes(int(self._instance.JointMode))

	@joint_mode.setter
	def joint_mode(self, value: JointModes):
		self._instance.JointMode = joint_modes(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
