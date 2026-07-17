from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Common import JointsValues as joints_values_1

T = typing.TypeVar('T')
class JointsValues1(typing.Generic[T]):
	'''Vector 6 of double values representing each robot joint'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joints_values_1()
		else:
			self._instance = _internal

	@property
	def base(self) -> T:
		'''Joint 1 out of 6'''
		return self._instance.Base

	@base.setter
	def base(self, value: T):
		self._instance.Base = value

	@property
	def shoulder(self) -> T:
		'''Joint 2 out of 6'''
		return self._instance.Shoulder

	@shoulder.setter
	def shoulder(self, value: T):
		self._instance.Shoulder = value

	@property
	def elbow(self) -> T:
		'''Joint 3 out of 6'''
		return self._instance.Elbow

	@elbow.setter
	def elbow(self, value: T):
		self._instance.Elbow = value

	@property
	def wrist1(self) -> T:
		'''Joint 4 out of 6'''
		return self._instance.Wrist1

	@wrist1.setter
	def wrist1(self, value: T):
		self._instance.Wrist1 = value

	@property
	def wrist2(self) -> T:
		'''Joint 5 out of 6'''
		return self._instance.Wrist2

	@wrist2.setter
	def wrist2(self, value: T):
		self._instance.Wrist2 = value

	@property
	def wrist3(self) -> T:
		'''Joint 6 out of 6'''
		return self._instance.Wrist3

	@wrist3.setter
	def wrist3(self, value: T):
		self._instance.Wrist3 = value

	@property
	def values(self) -> typing.List[T]:
		'''Array of the 6 joint data'''
		return list(self._instance.Values)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointsValues1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
