from __future__ import annotations
import typing
from underautomation.universal_robots.xml_rpc.xml_rpc_value import XmlRpcValue
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcStructMember as xml_rpc_struct_member

class XmlRpcStructMember:
	'''Member of a structure exchanged via XML-RPC'''
	def __init__(self, name: str, value: XmlRpcValue, _internal = 0):
		'''Initializes a new struct member with the specified name and value.

		:param name: The member name.
		:param value: The member value.
		'''
		if(_internal == 0):
			self._instance = xml_rpc_struct_member(name, value._instance if value else None)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		'''Determines whether the specified object is equal to this instance.

		:param obj: The object to compare with.
		:returns: true if the specified object is an XmlRpcStructMember with the same name and value; otherwise, false.
		'''
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		'''Returns a hash code for this instance.'''
		return self._instance.GetHashCode()

	@property
	def name(self) -> str:
		'''The name of this struct member.'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def value(self) -> XmlRpcValue:
		'''The value of this struct member.'''
		return XmlRpcValue(self._instance.Value)

	@value.setter
	def value(self, value: XmlRpcValue):
		self._instance.Value = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XmlRpcStructMember):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
