import typing
from __future__ import annotation
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from UnderAutomation.UniversalRobots.XmlRpc.Internal import XmlRpcServerBase as xml_rpc_server_base

class XmlRpcServerBase(URServiceBase):
	'''Base class providing XML-RPC server functionality for receiving remote procedure calls from a Universal Robots controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = xml_rpc_server_base()
		else:
			self._instance = _internal

	def xml_rpc_server_request(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.XmlRpcServerRequest+= lambda sender, request : handler(Wrapper(sender), Wrapper(request))

	def start(self, port: int) -> None:
		'''Enable the local XML-RPC server to receive commands from the robot

		:param port: Port number on which the server should start
		'''
		self._instance.Start(port)

	def stop(self) -> None:
		'''Disable and close the socket used for the XML-RPC server'''
		self._instance.Stop()

	@property
	def enabled(self) -> bool:
		'''Is the XML-RPC server enabled'''
		return self._instance.Enabled

	@property
	def port(self) -> int:
		'''Local port on which the XML-RPC server is running. 0 if server is disabled'''
		return self._instance.Port

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XmlRpcServerBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
