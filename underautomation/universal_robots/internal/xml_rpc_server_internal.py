import typing
from __future__ import annotation
from underautomation.universal_robots.xml_rpc.internal.xml_rpc_server_base import XmlRpcServerBase
from UnderAutomation.UniversalRobots.Internal import XmlRpcServerInternal as xml_rpc_server_internal

class XmlRpcServerInternal(XmlRpcServerBase):
	'''Internal implementation of the XML-RPC server used to expose methods callable by URScript programs on the robot.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = xml_rpc_server_internal()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XmlRpcServerInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
