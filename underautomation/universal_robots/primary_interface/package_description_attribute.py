from __future__ import annotations
import typing
from underautomation.universal_robots.primary_interface.package_unit import PackageUnit
from UnderAutomation.UniversalRobots.PrimaryInterface import PackageDescriptionAttribute as package_description_attribute
from UnderAutomation.UniversalRobots.PrimaryInterface import PackageUnit as package_unit

class PackageDescriptionAttribute:
	'''Describes a field of a received package'''
	def __init__(self, description: str, unit: PackageUnit, _internal = 0):
		'''Initializes a new instance with a specified physical unit.

		:param description: Human-readable description of the field.
		:param unit: Physical unit of the measured value.
		'''
		if(_internal == 0):
			self._instance = package_description_attribute(description, package_unit(int(unit)))
		else:
			self._instance = _internal

	@property
	def unit(self) -> PackageUnit:
		'''Physical unit of the field'''
		return PackageUnit(int(self._instance.Unit))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PackageDescriptionAttribute):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
