from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Common import ConnectException as connect_exception

class ConnectException:
	'''Exception thrown when connection to the robot fails'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = connect_exception()
		else:
			self._instance = _internal

	@property
	def service(self) -> str:
		'''Name of the robot service that failed to connect (e.g. Dashboard, RTDE, PrimaryInterface).'''
		return self._instance.Service

	@property
	def robot_ip(self) -> str:
		'''IP address of the robot that the connection was attempted to.'''
		return self._instance.RobotIp

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ConnectException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
