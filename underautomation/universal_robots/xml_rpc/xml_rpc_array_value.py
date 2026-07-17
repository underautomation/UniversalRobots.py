from __future__ import annotations
import typing
from underautomation.universal_robots.xml_rpc.xml_rpc_type import XmlRpcType
from underautomation.universal_robots.xml_rpc.xml_rpc_value import XmlRpcValue
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcArrayValue as xml_rpc_array_value
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcType as xml_rpc_type

class XmlRpcArrayValue(XmlRpcValue):
	'''Represents an array of XmlRpcValue that can be exchange with the robot via XML-RPC'''
	def __init__(self, value: typing.Any, _internal = 0):
		if(_internal == 0):
			self._instance = xml_rpc_array_value(value)
		else:
			self._instance = _internal

	@property
	def type(self) -> XmlRpcType:
		'''Gets the XML-RPC type of this value.'''
		return XmlRpcType(int(self._instance.Type))

	@property
	def value(self) -> typing.Any:
		'''The list of XML-RPC values contained in this array.'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XmlRpcArrayValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
