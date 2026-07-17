from __future__ import annotations
import typing
from underautomation.universal_robots.xml_rpc.xml_rpc_type import XmlRpcType
from underautomation.universal_robots.xml_rpc.xml_rpc_value import XmlRpcValue
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcIntegerValue as xml_rpc_integer_value
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcType as xml_rpc_type

class XmlRpcIntegerValue(XmlRpcValue):
	'''Represents an integer value that can be exchange with the robot via XML-RPC'''
	def __init__(self, value: int, _internal = 0):
		'''Initializes a new instance with the specified integer value.

		:param value: The integer value.
		'''
		if(_internal == 0):
			self._instance = xml_rpc_integer_value(value)
		else:
			self._instance = _internal

	@property
	def type(self) -> XmlRpcType:
		'''Gets the XML-RPC type of this value.'''
		return XmlRpcType(int(self._instance.Type))

	@property
	def value(self) -> int:
		'''The integer value.'''
		return self._instance.Value

	@value.setter
	def value(self, value: int):
		self._instance.Value = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XmlRpcIntegerValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
