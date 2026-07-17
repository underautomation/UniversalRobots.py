from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Dashboard import PolyscopeVersion as polyscope_version

class PolyscopeVersion:
	'''Describes a Polyscope version (robot controller firmware).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = polyscope_version()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		'''Determines whether the specified object is equal to this Polyscope version.'''
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		'''Returns a hash code for this Polyscope version.'''
		return self._instance.GetHashCode()

	@property
	def date(self) -> str:
		'''Release date (example : "Nov 2020")'''
		return self._instance.Date

	@date.setter
	def date(self, value: str):
		self._instance.Date = value

	@property
	def version(self) -> typing.Any:
		'''Firmware version'''
		return self._instance.Version

	@version.setter
	def version(self, value: typing.Any):
		self._instance.Version = value

	@property
	def description(self) -> str:
		'''String description of the firmware version (exemple : "5.0.16.8524 (Nov 2020)")'''
		return self._instance.Description

	@description.setter
	def description(self, value: str):
		self._instance.Description = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PolyscopeVersion):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
