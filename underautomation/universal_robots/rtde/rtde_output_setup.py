import typing
from __future__ import annotation
from underautomation.universal_robots.rtde.internal.rtde_setup_2 import RtdeSetup2
from underautomation.universal_robots.rtde.rtde_output_setup_item import RtdeOutputSetupItem
from underautomation.universal_robots.rtde.rtde_output_data import RtdeOutputData
from UnderAutomation.UniversalRobots.Rtde import RtdeOutputSetup as rtde_output_setup
from UnderAutomation.UniversalRobots.Rtde import RtdeOutputData as rtde_output_data

class RtdeOutputSetup(RtdeSetup2[RtdeOutputSetupItem, RtdeOutputData]):
	'''Defines the set of RTDE output variables (robot-to-client) to subscribe to as a recipe. The Timestamp variable is added by default.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance with the default Timestamp variable.'''
		if(_internal == 0):
			self._instance = rtde_output_setup()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeOutputSetup):
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
