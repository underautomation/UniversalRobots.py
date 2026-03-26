import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Ssh.Tools import IForwardedPort as i_forwarded_port

class IForwardedPort:
	'''Supports port forwarding functionality.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_forwarded_port()
		else:
			self._instance = _internal

	def closing(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.Closing+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IForwardedPort):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
