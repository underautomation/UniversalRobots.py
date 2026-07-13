from __future__ import annotations
import typing
from underautomation.universal_robots.xml_rpc.xml_rpc_type import XmlRpcType
from underautomation.universal_robots.common.pose import Pose
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcValue as xml_rpc_value
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcType as xml_rpc_type

class XmlRpcValue:
	'''Base class of all elements transmitted by XML-RPC. The Type property indicates the type into which this object can be cast to obtain the value.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = xml_rpc_value()
		else:
			self._instance = _internal

	@property
	def type(self) -> XmlRpcType:
		'''Determines the class of this message'''
		return XmlRpcType(int(self._instance.Type))

	@property
	def xml(self) -> typing.Any:
		'''The XML description of the message that has been received from the robot or will be sent to the robot'''
		return self._instance.Xml

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XmlRpcValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
