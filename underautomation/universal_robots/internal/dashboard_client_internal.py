from __future__ import annotations
import typing
from underautomation.universal_robots.dashboard.internal.dashboard_client_base import DashboardClientBase
from UnderAutomation.UniversalRobots.Internal import DashboardClientInternal as dashboard_client_internal

class DashboardClientInternal(DashboardClientBase):
	'''Internal implementation of the Dashboard Server client that delegates connection to the parent UR instance.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dashboard_client_internal()
		else:
			self._instance = _internal

	def enable(self, port: int=29999, receiveTimeoutMs: int=2000, sendTimeoutMs: int=500) -> None:
		'''Enable Dashboard client connection'''
		self._instance.Enable(port, receiveTimeoutMs, sendTimeoutMs)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DashboardClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
