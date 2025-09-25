import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Kinematics import TransformationSet as transformation_set

class TransformationSet:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = transformation_set()
		else:
			self._instance = _internal
	@property
	def base(self) -> typing.List[float]:
		return self._instance.Base
	@base.setter
	def base(self, value: typing.List[float]):
		self._instance.Base = value
	@property
	def shoulder(self) -> typing.List[float]:
		return self._instance.Shoulder
	@shoulder.setter
	def shoulder(self, value: typing.List[float]):
		self._instance.Shoulder = value
	@property
	def elbow(self) -> typing.List[float]:
		return self._instance.Elbow
	@elbow.setter
	def elbow(self, value: typing.List[float]):
		self._instance.Elbow = value
	@property
	def wrist1(self) -> typing.List[float]:
		return self._instance.Wrist1
	@wrist1.setter
	def wrist1(self, value: typing.List[float]):
		self._instance.Wrist1 = value
	@property
	def wrist2(self) -> typing.List[float]:
		return self._instance.Wrist2
	@wrist2.setter
	def wrist2(self, value: typing.List[float]):
		self._instance.Wrist2 = value
	@property
	def wrist3(self) -> typing.List[float]:
		return self._instance.Wrist3
	@wrist3.setter
	def wrist3(self, value: typing.List[float]):
		self._instance.Wrist3 = value
