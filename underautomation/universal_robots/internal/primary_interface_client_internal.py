import typing
from __future__ import annotation
from underautomation.universal_robots.primary_interface.interfaces import Interfaces
from underautomation.universal_robots.primary_interface.internal.primary_interface_client_base import PrimaryInterfaceClientBase
from UnderAutomation.UniversalRobots.Internal import PrimaryInterfaceClientInternal as primary_interface_client_internal
from UnderAutomation.UniversalRobots.PrimaryInterface import Interfaces as interfaces

class PrimaryInterfaceClientInternal(PrimaryInterfaceClientBase):
	'''Internal implementation of the Primary Interface client that delegates connection to the parent UR instance.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = primary_interface_client_internal()
		else:
			self._instance = _internal

	def connect(self, port: Interfaces) -> None:
		'''Connect to a specific interface

		:param port: Interface to connect to
		'''
		self._instance.Connect(interfaces(int(port)))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PrimaryInterfaceClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
