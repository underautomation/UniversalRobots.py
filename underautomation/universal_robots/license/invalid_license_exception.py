import typing
from __future__ import annotation
from underautomation.universal_robots.license.license_info import LicenseInfo
from UnderAutomation.UniversalRobots.License import InvalidLicenseException as invalid_license_exception

class InvalidLicenseException:
	'''Exception thrown while using the product if the license is not valid.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = invalid_license_exception()
		else:
			self._instance = _internal

	@property
	def license_info(self) -> LicenseInfo:
		'''The license that causes this exception'''
		return LicenseInfo(None, None, self._instance.LicenseInfo)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, InvalidLicenseException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
