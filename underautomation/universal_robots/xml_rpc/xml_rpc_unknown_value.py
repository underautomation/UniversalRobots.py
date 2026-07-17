from __future__ import annotations
import typing
from underautomation.universal_robots.xml_rpc.xml_rpc_type import XmlRpcType
from underautomation.universal_robots.xml_rpc.xml_rpc_value import XmlRpcValue
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcUnknownValue as xml_rpc_unknown_value
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcType as xml_rpc_type

class XmlRpcUnknownValue(XmlRpcValue):
	'''Represents an unknown XML-RPC argument that has been received from the robot You can decode it yourself with the XML property'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = xml_rpc_unknown_value()
		else:
			self._instance = _internal

	@property
	def type(self) -> XmlRpcType:
		'''Gets the XML-RPC type of this value.'''
		return XmlRpcType(int(self._instance.Type))

	@property
	def additional_information(self) -> str:
		'''Additional information about why this value could not be decoded.'''
		return self._instance.AdditionalInformation

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XmlRpcUnknownValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
