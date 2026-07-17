from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.internal.rtde_setup_2 import RtdeSetup2
from underautomation.universal_robots.rtde.rtde_input_setup_item import RtdeInputSetupItem
from underautomation.universal_robots.rtde.rtde_input_data import RtdeInputData
from UnderAutomation.UniversalRobots.Rtde import RtdeInputSetup as rtde_input_setup
from UnderAutomation.UniversalRobots.Rtde import RtdeInputData as rtde_input_data

class RtdeInputSetup(RtdeSetup2[RtdeInputSetupItem, RtdeInputData]):
	'''Defines the set of RTDE input variables (client-to-robot) to subscribe to as a recipe.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_input_setup()
		else:
			self._instance = _internal

	def add(self, data: RtdeInputData, index: int=0) -> RtdeInputSetupItem:
		'''Adds a variable to the recipe with the specified register index.

		:param data: The RTDE variable to add.
		:param index: Register index for array/register variables.
		:returns: The created setup item.
		'''
		return RtdeInputSetupItem(None, None, self._instance.Add(rtde_input_data(int(data)), index))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeInputSetup):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __iter__(self):
		enumerator = self._instance.GetEnumerator()
		while enumerator.MoveNext():
			yield enumerator.Current

	def __len__(self) -> int:
		return self._instance.Count
