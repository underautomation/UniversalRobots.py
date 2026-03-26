import typing
from __future__ import annotation
from underautomation.universal_robots.common.internal_error_event_args import InternalErrorEventArgs
from UnderAutomation.UniversalRobots.Internal import URServiceBase as ur_service_base

class URServiceBase:
	'''Base class of all UR services implemented in this SDK'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ur_service_base()
		else:
			self._instance = _internal

	def internal_error_occured(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.InternalErrorOccured+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, URServiceBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
