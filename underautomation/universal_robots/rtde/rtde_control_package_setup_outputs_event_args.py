import typing
from __future__ import annotation
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.Rtde import RtdeControlPackageSetupOutputsEventArgs as rtde_control_package_setup_outputs_event_args

class RtdeControlPackageSetupOutputsEventArgs(PackageEventArgs):
	'''Event arguments raised when the robot acknowledges the RTDE output recipe setup.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_control_package_setup_outputs_event_args()
		else:
			self._instance = _internal

	@property
	def output_recipe_id(self) -> int:
		'''Gets or sets the recipe identifier assigned by the robot for output data.'''
		return self._instance.OutputRecipeId

	@output_recipe_id.setter
	def output_recipe_id(self, value: int):
		self._instance.OutputRecipeId = value

	@property
	def variable_types(self) -> typing.List[str]:
		'''Gets or sets the status of each subscribed output variable. Each entry contains the RTDE type name, or "IN_USE" / "NOT_FOUND".'''
		return self._instance.VariableTypes

	@variable_types.setter
	def variable_types(self, value: typing.List[str]):
		self._instance.VariableTypes = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeControlPackageSetupOutputsEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
