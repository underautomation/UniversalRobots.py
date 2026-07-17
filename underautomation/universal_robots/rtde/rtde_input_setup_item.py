from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.rtde_input_data import RtdeInputData
from underautomation.universal_robots.rtde.rtde_data_description_1 import RtdeDataDescription1
from underautomation.universal_robots.rtde.internal.rtde_setup_item_1 import RtdeSetupItem1
from UnderAutomation.UniversalRobots.Rtde import RtdeInputSetupItem as rtde_input_setup_item
from UnderAutomation.UniversalRobots.Rtde import RtdeInputData as rtde_input_data

class RtdeInputSetupItem(RtdeSetupItem1[RtdeInputData]):
	'''Represents a single RTDE input variable (client-to-robot) in an input recipe.'''
	def __init__(self, data: RtdeInputData, index: int, _internal = 0):
		'''Initializes a new instance for the specified input variable and register index.

		:param data: The RTDE input variable.
		:param index: Zero-based register index for array/register variables.
		'''
		if(_internal == 0):
			self._instance = rtde_input_setup_item(rtde_input_data(int(data)), index)
		else:
			self._instance = _internal

	@property
	def description(self) -> RtdeDataDescription1[RtdeInputData]:
		'''Gets the description metadata for this input variable.'''
		return RtdeDataDescription1[RtdeInputData](self._instance.Description)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeInputSetupItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
