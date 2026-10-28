from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Common import RobotDashboardResponse as robot_dashboard_response

class RobotDashboardResponse:
	'''Answer of a command of IRobotDashboard. The same type is returned by the Dashboard Server client (PolyScope 5) and by the REST API client (PolyScope X), so that one code works with both. The other methods of the two clients keep their own answer types (CommandResponse and RestApiResponse).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_dashboard_response()
		else:
			self._instance = _internal

	@property
	def succeed(self) -> bool:
		'''Indicates that the robot accepted and executed the command.'''
		return self._instance.Succeed

	@succeed.setter
	def succeed(self, value: bool):
		self._instance.Succeed = value

	@property
	def message(self) -> str:
		'''Message of the robot, or description of the error.'''
		return self._instance.Message

	@message.setter
	def message(self, value: str):
		self._instance.Message = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotDashboardResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
