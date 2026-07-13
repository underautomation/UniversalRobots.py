from __future__ import annotations
import typing
from underautomation.universal_robots.xml_rpc.xml_rpc_value import XmlRpcValue
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcEventArg as xml_rpc_event_arg

class XmlRpcEventArg:
	'''Represents a request that has just been received from the robot'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = xml_rpc_event_arg()
		else:
			self._instance = _internal

	@property
	def xml_request(self) -> typing.Any:
		'''The XML document received via HTTP'''
		return self._instance.XmlRequest

	@property
	def method_name(self) -> str:
		'''The method called by the robot'''
		return self._instance.MethodName

	@property
	def arguments(self) -> typing.List[XmlRpcValue]:
		'''The arguments of the method called'''
		return [XmlRpcValue(x) for x in self._instance.Arguments]

	@property
	def end_point(self) -> typing.Any:
		'''IP address of the robot'''
		return self._instance.EndPoint

	@property
	def answer(self) -> XmlRpcValue:
		'''Response to be provided to the robot by the user'''
		return XmlRpcValue(self._instance.Answer)

	@answer.setter
	def answer(self, value: XmlRpcValue):
		self._instance.Answer = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XmlRpcEventArg):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
