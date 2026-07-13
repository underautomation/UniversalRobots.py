from __future__ import annotations
import typing
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import VersionEventArgs as version_event_args

class VersionEventArgs(PackageEventArgs):
	'''Version information from the robot controller firmware'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = version_event_args()
		else:
			self._instance = _internal

	@property
	def project_name(self) -> str:
		'''URControl project'''
		return self._instance.ProjectName

	@project_name.setter
	def project_name(self, value: str):
		self._instance.ProjectName = value

	@property
	def major_version(self) -> int:
		'''Major version number, for example 5 in 5.6.1.1234'''
		return self._instance.MajorVersion

	@major_version.setter
	def major_version(self, value: int):
		self._instance.MajorVersion = value

	@property
	def minor_version(self) -> int:
		'''Minor firmware version number, for example 6 in 5.6.1.1234'''
		return self._instance.MinorVersion

	@minor_version.setter
	def minor_version(self, value: int):
		self._instance.MinorVersion = value

	@property
	def bugfix_version(self) -> int:
		'''Firmware bugfix number, for example 1 in 5.6.1.1234'''
		return self._instance.BugfixVersion

	@bugfix_version.setter
	def bugfix_version(self, value: int):
		self._instance.BugfixVersion = value

	@property
	def build_number(self) -> int:
		'''Firmware build number, for example 1234 in 5.6.1.1234'''
		return self._instance.BuildNumber

	@build_number.setter
	def build_number(self, value: int):
		self._instance.BuildNumber = value

	@property
	def build_date(self) -> str:
		'''Build date of the firmware, for example "DEC 2020"'''
		return self._instance.BuildDate

	@build_date.setter
	def build_date(self, value: str):
		self._instance.BuildDate = value

	@property
	def version(self) -> typing.Any:
		'''Version of the firmware'''
		return self._instance.Version

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VersionEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
