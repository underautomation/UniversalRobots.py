import typing
from __future__ import annotation
from underautomation.universal_robots.xml_rpc.xml_rpc_type import XmlRpcType
from underautomation.universal_robots.xml_rpc.xml_rpc_value import XmlRpcValue
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcBooleanValue as xml_rpc_boolean_value
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcType as xml_rpc_type

class XmlRpcBooleanValue(XmlRpcValue):
	'''Represents a boolean value that can be exchange with the robot via XML-RPC'''
	def __init__(self, value: bool, _internal = 0):
		'''Initializes a new instance with the specified boolean value.

		:param value: The boolean value.
		'''
		if(_internal == 0):
			self._instance = xml_rpc_boolean_value(value)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		'''Determines whether the specified object is equal to this instance.

		:param obj: The object to compare with.
		:returns: true if the specified object is an XmlRpcBooleanValue with the same value; otherwise, false.
		'''
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		'''Returns a hash code for this instance.'''
		return self._instance.GetHashCode()

	@property
	def type(self) -> XmlRpcType:
		'''Gets the XML-RPC type of this value.'''
		return XmlRpcType(int(self._instance.Type))

	@property
	def value(self) -> bool:
		'''The boolean value.'''
		return self._instance.Value

	@value.setter
	def value(self, value: bool):
		self._instance.Value = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XmlRpcBooleanValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
