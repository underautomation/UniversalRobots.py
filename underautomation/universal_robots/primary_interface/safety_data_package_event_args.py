import typing
from __future__ import annotation
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import SafetyDataPackageEventArgs as safety_data_package_event_args

class SafetyDataPackageEventArgs(PackageEventArgs):
	'''Safety internal data'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = safety_data_package_event_args()
		else:
			self._instance = _internal

	@property
	def data(self) -> typing.List[int]:
		'''Irrelevant (Internal use only)'''
		return self._instance.Data

	@data.setter
	def data(self, value: typing.List[int]):
		self._instance.Data = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SafetyDataPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
