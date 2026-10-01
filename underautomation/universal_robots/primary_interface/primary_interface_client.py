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

	@typing.overload
	def connect(self, ip: str, port: Interfaces) -> None: ...

	@typing.overload
	def connect(self, ip: str) -> None: ...

	def connect(self, *args, **kwargs) -> None:
		'''Connect to a specific port
		Connect to primary interface

		Arguments: (ip, port)
		Arguments: (ip)
		:param ip: Robot IP address.
		:param port: Robot port.
		'''
		__a = _bind_overload(args, kwargs, ['ip', 'port'], {})
		if __a is not None:
			ip, port = __a
			self._instance.Connect(ip, interfaces(int(port)))
			return
		__a = _bind_overload(args, kwargs, ['ip'], {})
		if __a is not None:
			ip, = __a
			self._instance.Connect(ip)
			return
		raise TypeError("connect(): no overload takes these arguments")

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

def _bind_overload(args, kwargs, names, defaults):
	if len(args) > len(names) or any(k not in names[len(args):] for k in kwargs):
		return None
	values = list(args)
	for name in names[len(args):]:
		if name in kwargs:
			values.append(kwargs[name])
		elif name in defaults:
			values.append(defaults[name])
		else:
			return None
	return values
