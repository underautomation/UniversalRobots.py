from __future__ import annotations
import typing
from underautomation.universal_robots.primary_interface.interfaces import Interfaces
from underautomation.universal_robots.primary_interface.internal.primary_interface_client_base import PrimaryInterfaceClientBase
from UnderAutomation.UniversalRobots.PrimaryInterface import PrimaryInterfaceClient as primary_interface_client
from UnderAutomation.UniversalRobots.PrimaryInterface import Interfaces as interfaces

class PrimaryInterfaceClient(PrimaryInterfaceClientBase):
	'''Primary / Secondary interface implementation'''
	def __init__(self, _internal = 0):
		'''Creates a new Primary Interface client'''
		if(_internal == 0):
			self._instance = primary_interface_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, port: Interfaces) -> None:
		'''Connect to a specific port

		:param ip: Robot IP address
		:param port: Robot port
		'''
		self._instance.Connect(ip, interfaces(int(port)))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PrimaryInterfaceClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
