import typing
from __future__ import annotation
from underautomation.universal_robots.rtde.rtde_versions import RtdeVersions
from underautomation.universal_robots.rtde.rtde_output_setup import RtdeOutputSetup
from underautomation.universal_robots.rtde.rtde_input_setup import RtdeInputSetup
from UnderAutomation.UniversalRobots.Rtde.Internal import RtdeParametersBase as rtde_parameters_base
from UnderAutomation.UniversalRobots.Rtde import RtdeVersions as rtde_versions

class RtdeParametersBase:
	'''Base parameters to set up RTDE'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_parameters_base()
		else:
			self._instance = _internal

	@property
	def frequency(self) -> float:
		'''For RTDE version 2, you can specify a frequency for output received data. Maximum frequency depends on your robot version. If you set frequency to 0, maximum frequency will be choosen Default value is 10Hz'''
		return self._instance.Frequency

	@frequency.setter
	def frequency(self, value: float):
		self._instance.Frequency = value

	@property
	def version(self) -> RtdeVersions:
		'''RTDE version. If set to Auto, the most recent version will be choosen according to your robot version Default value is V2'''
		return RtdeVersions(int(self._instance.Version))

	@version.setter
	def version(self, value: RtdeVersions):
		self._instance.Version = rtde_versions(int(value))

	@property
	def output_setup(self) -> RtdeOutputSetup:
		'''List of all output data the robot will send to your application'''
		return RtdeOutputSetup(self._instance.OutputSetup)

	@output_setup.setter
	def output_setup(self, value: RtdeOutputSetup):
		self._instance.OutputSetup = value._instance if value else None

	@property
	def input_setup(self) -> RtdeInputSetup:
		'''List of all input data you can send to the robot'''
		return RtdeInputSetup(self._instance.InputSetup)

	@input_setup.setter
	def input_setup(self, value: RtdeInputSetup):
		self._instance.InputSetup = value._instance if value else None

	@property
	def port(self) -> int:
		'''TCP port used for RTDE connection. Default : 30004'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default RTDE TCP port used (30004)
RtdeParametersBase.DEFAULT_PORT = rtde_parameters_base.DEFAULT_PORT
