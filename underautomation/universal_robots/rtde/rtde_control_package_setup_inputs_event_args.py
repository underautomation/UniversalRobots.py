import typing
from __future__ import annotation
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.Rtde import RtdeControlPackageSetupInputsEventArgs as rtde_control_package_setup_inputs_event_args

class RtdeControlPackageSetupInputsEventArgs(PackageEventArgs):
	'''Event arguments raised when the robot acknowledges the RTDE input recipe setup.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_control_package_setup_inputs_event_args()
		else:
			self._instance = _internal

	@property
	def input_recipe_id(self) -> int:
		'''Recipe Identifier of input sent data'''
		return self._instance.InputRecipeId

	@input_recipe_id.setter
	def input_recipe_id(self, value: int):
		self._instance.InputRecipeId = value

	@property
	def variable_types(self) -> typing.List[str]:
		'''Status of each registers. Contains the type or the status IN_USE / NOT_FOUND'''
		return self._instance.VariableTypes

	@variable_types.setter
	def variable_types(self, value: typing.List[str]):
		self._instance.VariableTypes = value

	@property
	def input_recipe_is_valid(self) -> bool:
		'''Indicates that the recipe is valid, i.e. that all the registers have been found and are not already reserved for writing by another RTDE client. Check event SetupInputsReceived to see which registers are NOT_FOUND or IN_USE'''
		return self._instance.InputRecipeIsValid

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeControlPackageSetupInputsEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
