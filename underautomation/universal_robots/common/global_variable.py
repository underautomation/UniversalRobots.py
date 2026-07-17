from __future__ import annotations
import typing
from underautomation.universal_robots.common.global_variable_value import GlobalVariableValue
from UnderAutomation.UniversalRobots.Common import GlobalVariable as global_variable

class GlobalVariable(GlobalVariableValue):
	'''Describes a global variable'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = global_variable()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		'''Determines whether the specified object is a GlobalVariable with the same name, type, and value.'''
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		'''Returns a hash code based on the variable name, type, and value.'''
		return self._instance.GetHashCode()

	@property
	def name(self) -> str:
		'''Variable name'''
		return self._instance.Name

	@property
	def time(self) -> typing.Any:
		'''Last time the variable was sampled'''
		return self._instance.Time

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GlobalVariable):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
