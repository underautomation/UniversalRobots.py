import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.SocketCommunication import ISocketHandler as i_socket_handler

class ISocketHandler:
	'''Interface for classes that support socket messages'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_socket_handler()
		else:
			self._instance = _internal

	def socket_get_var(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.SocketGetVar+= lambda sender, request : handler(Wrapper(sender), Wrapper(request))

	def socket_request(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.SocketRequest+= lambda sender, request : handler(Wrapper(sender), Wrapper(request))

	def socket_client_disconnection(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.SocketClientDisconnection+= lambda sender, request : handler(Wrapper(sender), Wrapper(request))

	def socket_write(self, message: str) -> None:
		'''Write a socket message to the robot. The robot should be connected with socket_open()

		:param message: Message to send to the robot
		'''
		self._instance.SocketWrite(message)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ISocketHandler):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
