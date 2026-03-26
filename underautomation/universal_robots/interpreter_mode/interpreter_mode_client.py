import typing
from __future__ import annotation
from underautomation.universal_robots.interpreter_mode.internal.interpreter_mode_client_base import InterpreterModeClientBase
from UnderAutomation.UniversalRobots.InterpreterMode import InterpreterModeClient as interpreter_mode_client

class InterpreterModeClient(InterpreterModeClientBase):
	'''Client for the Universal Robots Interpreter Mode, allowing real-time execution of URScript commands over TCP.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = interpreter_mode_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, port: int=30020) -> None:
		'''Specifies the IP address of the robot. No TCP connection is maintained. A new connection is created when sending each command.

		:param ip: IP of the robot
		:param port: Robot interpreter mode port. Default : 30020
		'''
		self._instance.Connect(ip, port)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, InterpreterModeClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
