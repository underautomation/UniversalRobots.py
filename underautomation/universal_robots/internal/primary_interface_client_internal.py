from __future__ import annotations
import typing
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

	@typing.overload
	def connect(self, port: Interfaces) -> None: ...

	@typing.overload
	def connect(self) -> None: ...

	def connect(self, *args, **kwargs) -> None:
		'''Connect to a specific interface
		Connect to primary interface

		Arguments: (port)
		Arguments: ()
		:param port: Interface to connect to.
		'''
		__a = _bind_overload(args, kwargs, ['port'], {})
		if __a is not None:
			port, = __a
			self._instance.Connect(interfaces(int(port)))
			return
		__a = _bind_overload(args, kwargs, [], {})
		if __a is not None:
			self._instance.Connect()
			return
		raise TypeError("connect(): no overload takes these arguments")

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
