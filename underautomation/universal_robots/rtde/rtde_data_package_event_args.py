from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.rtde_output_values import RtdeOutputValues
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.Rtde import RtdeDataPackageEventArgs as rtde_data_package_event_args

class RtdeDataPackageEventArgs(PackageEventArgs):
	'''Event arguments for an RTDE output data package received from the robot at the subscribed frequency.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_data_package_event_args()
		else:
			self._instance = _internal

	@property
	def output_recipe_id(self) -> int:
		'''Gets or sets the recipe identifier for the received output data (RTDE v2 only; 0 for v1).'''
		return self._instance.OutputRecipeId

	@output_recipe_id.setter
	def output_recipe_id(self, value: int):
		self._instance.OutputRecipeId = value

	@property
	def output_data_values(self) -> RtdeOutputValues:
		'''Gets or sets the decoded output values contained in this data package.'''
		return RtdeOutputValues(self._instance.OutputDataValues)

	@output_data_values.setter
	def output_data_values(self, value: RtdeOutputValues):
		self._instance.OutputDataValues = value._instance if value else None

	@property
	def measured_frequency(self) -> float:
		'''Gets or sets the measured frequency in Hz, computed from successive Timestamp values.'''
		return self._instance.MeasuredFrequency

	@measured_frequency.setter
	def measured_frequency(self, value: float):
		self._instance.MeasuredFrequency = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeDataPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
