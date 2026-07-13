from __future__ import annotations
import typing
from underautomation.universal_robots.common.global_variable import GlobalVariable
from UnderAutomation.UniversalRobots.PrimaryInterface import GlobalVariablesEventArgs as global_variables_event_args

class GlobalVariablesEventArgs:
	'''Event args of variable update events'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = global_variables_event_args()
		else:
			self._instance = _internal

	@property
	def variables(self) -> typing.List[GlobalVariable]:
		'''New list of all up to date variables'''
		return [GlobalVariable(x) for x in self._instance.Variables]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GlobalVariablesEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
