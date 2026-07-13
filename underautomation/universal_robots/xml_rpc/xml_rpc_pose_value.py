from __future__ import annotations
import typing
from underautomation.universal_robots.common.pose import Pose
from underautomation.universal_robots.xml_rpc.xml_rpc_type import XmlRpcType
from underautomation.universal_robots.xml_rpc.xml_rpc_struct_value import XmlRpcStructValue
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcPoseValue as xml_rpc_pose_value
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcType as xml_rpc_type

class XmlRpcPoseValue(XmlRpcStructValue):
	'''Represents a pose value that can be exchange with the robot via XML-RPC'''
	def __init__(self, pose: Pose, _internal = 0):
		'''Creates a new pose Value'''
		if(_internal == 0):
			self._instance = xml_rpc_pose_value(pose._instance if pose else None)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		'''Determines whether the specified object is equal to this instance.

		:param obj: The object to compare with.
		:returns: true if the specified object is an XmlRpcPoseValue with the same pose; otherwise, false.
		'''
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		'''Returns a hash code for this instance.'''
		return self._instance.GetHashCode()

	@property
	def value(self) -> Pose:
		'''Pose Value'''
		return Pose(None, None, None, None, None, None, self._instance.Value)

	@property
	def type(self) -> XmlRpcType:
		'''Returns type : XmlRpcType.Pose'''
		return XmlRpcType(int(self._instance.Type))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XmlRpcPoseValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
