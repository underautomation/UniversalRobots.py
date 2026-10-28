from __future__ import annotations
import typing
from underautomation.universal_robots.common.global_variable_types import GlobalVariableTypes
from underautomation.universal_robots.common.pose import Pose
from UnderAutomation.UniversalRobots.Common import GlobalVariableValue as global_variable_value
from UnderAutomation.UniversalRobots.Common import GlobalVariableTypes as global_variable_types

class GlobalVariableValue:
	'''Describes a typed variable value'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = global_variable_value()
		else:
			self._instance = _internal

	def to_list(self) -> typing.List['GlobalVariableValue']:
		'''Returns an array of GlobalVariableValue if Type is List. Else, null is returned'''
		__r = self._instance.ToList()
		return None if __r is None else [None if x is None else GlobalVariableValue(x) for x in __r]

	def to_pose(self) -> Pose:
		'''Returns a Pose if Type is Pose. Else, null is returned'''
		__r = self._instance.ToPose()
		return None if __r is None else Pose(None, None, None, None, None, None, __r)

	def to_bool(self) -> bool:
		'''Returns variable value if type is Bool. Il type is Float or Int, it returns True if value is not 0. Else, it returns false'''
		return self._instance.ToBool()

	def to_int(self) -> int:
		'''Returns variable value if type is Int. Il type is Float, it tries to cast it to int. If Type is bool, it returns 1 or 0. Else it returns 0'''
		return self._instance.ToInt()

	def to_float(self) -> float:
		'''Returns variable value if type is Float. Il type is int, it casts it to float. If Type is bool, it returns 1 or 0. Else it returns NaN'''
		return self._instance.ToFloat()

	@staticmethod
	def parse(message: str) -> 'GlobalVariableValue':
		'''Estimate variable value from its string representation'''
		__r = global_variable_value.Parse(message)
		return None if __r is None else GlobalVariableValue(__r)

	@property
	def type(self) -> GlobalVariableTypes:
		'''Type of a variable'''
		return GlobalVariableTypes(int(self._instance.Type))

	@property
	def value(self) -> typing.Any:
		'''Value of the variable'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GlobalVariableValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
