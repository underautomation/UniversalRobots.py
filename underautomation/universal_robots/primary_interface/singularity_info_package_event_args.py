from __future__ import annotations
import typing
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import SingularityInfoPackageEventArgs as singularity_info_package_event_args

class SingularityInfoPackageEventArgs(PackageEventArgs):
	'''Singularity info'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = singularity_info_package_event_args()
		else:
			self._instance = _internal

	@property
	def singularity_severity(self) -> int:
		'''Severity of the singularity'''
		return self._instance.SingularitySeverity

	@singularity_severity.setter
	def singularity_severity(self, value: int):
		self._instance.SingularitySeverity = value

	@property
	def singularity_type(self) -> int:
		'''Type of the singularity'''
		return self._instance.SingularityType

	@singularity_type.setter
	def singularity_type(self, value: int):
		self._instance.SingularityType = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SingularityInfoPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
