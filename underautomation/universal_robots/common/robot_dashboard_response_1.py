from __future__ import annotations
import typing
from underautomation.universal_robots.common.robot_dashboard_response import RobotDashboardResponse
from UnderAutomation.UniversalRobots.Common import RobotDashboardResponse as robot_dashboard_response_1

T = typing.TypeVar('T')
class RobotDashboardResponse1(RobotDashboardResponse, typing.Generic[T]):
	'''Answer of a command of IRobotDashboard that returns a value.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_dashboard_response_1()
		else:
			self._instance = _internal

	@property
	def value(self) -> T:
		'''Value returned by the command. It is meaningful only if succeed is true.'''
		return self._instance.Value

	@value.setter
	def value(self, value: T):
		self._instance.Value = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotDashboardResponse1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
