from __future__ import annotations
import typing
from underautomation.universal_robots.xml_rpc.internal.xml_rpc_parameters_base import XmlRpcParametersBase
from UnderAutomation.UniversalRobots.Common import XmlRpcConnectParameters as xml_rpc_connect_parameters

class XmlRpcConnectParameters(XmlRpcParametersBase):
	'''Setup XML-RPC server'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = xml_rpc_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Enable XML-RPC server'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XmlRpcConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
