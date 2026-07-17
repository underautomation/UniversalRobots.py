from __future__ import annotations
import typing
from underautomation.universal_robots.kinematics.transformation_set import TransformationSet
from UnderAutomation.UniversalRobots.Kinematics import KinematicsResult as kinematics_result

class KinematicsResult:
	'''Result of a forward kinematics calculation'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kinematics_result()
		else:
			self._instance = _internal

	@property
	def tool_transform(self) -> typing.List[float]:
		'''4x4 transformation matrix of the tool'''
		return self._instance.ToolTransform

	@tool_transform.setter
	def tool_transform(self, value: typing.List[float]):
		self._instance.ToolTransform = value

	@property
	def individual_local_transforms(self) -> TransformationSet:
		'''Individual local transformation matrices of each joint'''
		return TransformationSet(self._instance.IndividualLocalTransforms)

	@individual_local_transforms.setter
	def individual_local_transforms(self, value: TransformationSet):
		self._instance.IndividualLocalTransforms = value._instance if value else None

	@property
	def cumulative_global_transforms(self) -> TransformationSet:
		'''Cumulative global transformation matrices of each joint'''
		return TransformationSet(self._instance.CumulativeGlobalTransforms)

	@cumulative_global_transforms.setter
	def cumulative_global_transforms(self, value: TransformationSet):
		self._instance.CumulativeGlobalTransforms = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, KinematicsResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
