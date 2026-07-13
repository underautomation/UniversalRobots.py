from __future__ import annotations
import typing
from underautomation.universal_robots.socket_communication.i_socket_handler import ISocketHandler
from underautomation.universal_robots.socket_communication.socket_client import SocketClient
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from UnderAutomation.UniversalRobots.SocketCommunication.Internal import SocketCommunicationServerBase as socket_communication_server_base

class SocketCommunicationServerBase(URServiceBase, ISocketHandler):
	'''Base for Socket communication server'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = socket_communication_server_base()
		else:
			self._instance = _internal

	def socket_client_connection(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.SocketClientConnection+= lambda sender, request : handler(Wrapper(sender), Wrapper(request))

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

	def start(self, port: int) -> None:
		'''Starts socket server. Robot can connect with URScript function socket_open()

		:param port: Socket server port
		'''
		self._instance.Start(port)

	def stop(self) -> None:
		'''Disable local socket server and disconnect all connected clients'''
		self._instance.Stop()

	def socket_write(self, message: str) -> None:
		'''Write a socket message to the robot. The robot should be connected with socket_open()

		:param message: Message to send to the robot
		'''
		self._instance.SocketWrite(message)

	@property
	def connected_clients(self) -> typing.List[SocketClient]:
		'''List of all connected clients. One robot can open multiple sockets.'''
		return [SocketClient(x) for x in self._instance.ConnectedClients]

	@property
	def enabled(self) -> bool:
		'''Is the socket server enabled'''
		return self._instance.Enabled

	@property
	def port(self) -> int:
		'''Socket server local port'''
		return self._instance.Port

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SocketCommunicationServerBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
