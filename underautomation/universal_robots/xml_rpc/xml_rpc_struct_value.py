import typing
from underautomation.universal_robots.xml_rpc.xml_rpc_type import XmlRpcType
from underautomation.universal_robots.xml_rpc.xml_rpc_value import XmlRpcValue
from underautomation.universal_robots.xml_rpc.xml_rpc_struct_member import XmlRpcStructMember
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcStructValue as xml_rpc_struct_value

class XmlRpcStructValue(XmlRpcValue):
	def __init__(self, value: typing.Any, _internal = 0):
		if(_internal == 0):
			self._instance = xml_rpc_struct_value(value)
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def type(self) -> XmlRpcType:
		return XmlRpcType(self._instance.Type)
	@property
	def value(self) -> typing.Any:
		return self._instance.Value
