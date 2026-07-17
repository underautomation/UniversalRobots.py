from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Kinematics import TransformationSet as transformation_set

class TransformationSet:
	'''Set of transformation matrices for each joint'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = transformation_set()
		else:
			self._instance = _internal

	@property
	def base(self) -> typing.List[float]:
		'''4x4 transformation matrix of the base joint 1'''
		return self._instance.Base

	@base.setter
	def base(self, value: typing.List[float]):
		self._instance.Base = value

	@property
	def shoulder(self) -> typing.List[float]:
		'''4x4 transformation matrix of the shoulder joint 2'''
		return self._instance.Shoulder

	@shoulder.setter
	def shoulder(self, value: typing.List[float]):
		self._instance.Shoulder = value

	@property
	def elbow(self) -> typing.List[float]:
		'''4x4 transformation matrix of the elbow joint 3'''
		return self._instance.Elbow

	@elbow.setter
	def elbow(self, value: typing.List[float]):
		self._instance.Elbow = value

	@property
	def wrist1(self) -> typing.List[float]:
		'''4x4 transformation matrix of the wrist1 joint 4'''
		return self._instance.Wrist1

	@wrist1.setter
	def wrist1(self, value: typing.List[float]):
		self._instance.Wrist1 = value

	@property
	def wrist2(self) -> typing.List[float]:
		'''4x4 transformation matrix of the wrist2 joint 5'''
		return self._instance.Wrist2

	@wrist2.setter
	def wrist2(self, value: typing.List[float]):
		self._instance.Wrist2 = value

	@property
	def wrist3(self) -> typing.List[float]:
		'''4x4 transformation matrix of the wrist3 (Tool) joint 6'''
		return self._instance.Wrist3

	@wrist3.setter
	def wrist3(self, value: typing.List[float]):
		self._instance.Wrist3 = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TransformationSet):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
