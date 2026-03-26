import typing
from __future__ import annotation
from underautomation.universal_robots.xml_rpc.xml_rpc_type import XmlRpcType
from underautomation.universal_robots.xml_rpc.xml_rpc_value import XmlRpcValue
from underautomation.universal_robots.xml_rpc.xml_rpc_struct_member import XmlRpcStructMember
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcStructValue as xml_rpc_struct_value
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcType as xml_rpc_type

class XmlRpcStructValue(XmlRpcValue):
	'''Represents a structure that can be exchange with the robot via XML-RPC'''
	def __init__(self, value: typing.Any, _internal = 0):
		if(_internal == 0):
			self._instance = xml_rpc_struct_value(value)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		'''Determines whether the specified object is equal to this instance.

		:param obj: The object to compare with.
		:returns: true if the specified object is an XmlRpcStructValue with the same members; otherwise, false.
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
	def value(self) -> typing.Any:
		'''The list of key-value members in this structure.'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XmlRpcStructValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
