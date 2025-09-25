import typing
from underautomation.universal_robots.kinematics.transformation_set import TransformationSet
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Kinematics import KinematicsResult as kinematics_result

class KinematicsResult:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kinematics_result()
		else:
			self._instance = _internal
	@property
	def tool_transform(self) -> typing.List[float]:
		return self._instance.ToolTransform
	@tool_transform.setter
	def tool_transform(self, value: typing.List[float]):
		self._instance.ToolTransform = value
	@property
	def individual_local_transforms(self) -> TransformationSet:
		return TransformationSet(self._instance.IndividualLocalTransforms)
	@individual_local_transforms.setter
	def individual_local_transforms(self, value: TransformationSet):
		self._instance.IndividualLocalTransforms = value
	@property
	def cumulative_global_transforms(self) -> TransformationSet:
		return TransformationSet(self._instance.CumulativeGlobalTransforms)
	@cumulative_global_transforms.setter
	def cumulative_global_transforms(self, value: TransformationSet):
		self._instance.CumulativeGlobalTransforms = value
