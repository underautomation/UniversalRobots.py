from __future__ import annotations
import typing
from underautomation.universal_robots.primary_interface.interfaces import Interfaces
from UnderAutomation.UniversalRobots.PrimaryInterface.Internal import PrimaryInterfaceParametersBase as primary_interface_parameters_base
from UnderAutomation.UniversalRobots.PrimaryInterface import Interfaces as interfaces

class PrimaryInterfaceParametersBase:
	'''Parameters to setup a Primary/secondary interface connection'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = primary_interface_parameters_base()
		else:
			self._instance = _internal

	@property
	def port(self) -> Interfaces:
		'''Interface on which to connect'''
		return Interfaces(int(self._instance.Port))

	@port.setter
	def port(self, value: Interfaces):
		self._instance.Port = interfaces(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PrimaryInterfaceParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
