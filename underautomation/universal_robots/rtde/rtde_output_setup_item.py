import typing
from __future__ import annotation
from underautomation.universal_robots.rtde.rtde_output_data import RtdeOutputData
from underautomation.universal_robots.rtde.rtde_data_description_1 import RtdeDataDescription1
from underautomation.universal_robots.rtde.internal.rtde_setup_item_1 import RtdeSetupItem1
from UnderAutomation.UniversalRobots.Rtde import RtdeOutputSetupItem as rtde_output_setup_item
from UnderAutomation.UniversalRobots.Rtde import RtdeOutputData as rtde_output_data

class RtdeOutputSetupItem(RtdeSetupItem1[RtdeOutputData]):
	'''Represents a single RTDE output variable (robot-to-client) in an output recipe.'''
	def __init__(self, data: RtdeOutputData, index: int, _internal = 0):
		'''Initializes a new instance for the specified output variable and register index.

		:param data: The RTDE output variable.
		:param index: Zero-based register index for array/register variables.
		'''
		if(_internal == 0):
			self._instance = rtde_output_setup_item(data, index)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def description(self) -> RtdeDataDescription1[RtdeOutputData]:
		'''Gets the description metadata for this output variable.'''
		return RtdeDataDescription1[RtdeOutputData](self._instance.Description)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeOutputSetupItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
