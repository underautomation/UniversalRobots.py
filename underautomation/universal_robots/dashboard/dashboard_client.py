from __future__ import annotations
import typing
from underautomation.universal_robots.dashboard.internal.dashboard_client_base import DashboardClientBase
from UnderAutomation.UniversalRobots.Dashboard import DashboardClient as dashboard_client

class DashboardClient(DashboardClientBase):
	'''Client for the Universal Robots Dashboard Server protocol. Enables remote control of the robot (load/play/stop programs, power on/off, etc.) via TCP commands on port 29999.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dashboard_client()
		else:
			self._instance = _internal

	def enable(self, ip: str, port: int=29999, receiveTimeoutMs: int=2000, sendTimeoutMs: int=500) -> None:
		'''Specifies the IP address of the robot. No TCP connection is maintained. A new connection is created when sending each command.

		:param ip: IP of the robot
		:param port: Robot dashboard server port. Default : 29999
		:param receiveTimeoutMs: Receive timeout in milliseconds. Default : 2000 ms
		:param sendTimeoutMs: Send timeout in milliseconds. Default : 500 ms
		'''
		self._instance.Enable(ip, port, receiveTimeoutMs, sendTimeoutMs)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DashboardClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
