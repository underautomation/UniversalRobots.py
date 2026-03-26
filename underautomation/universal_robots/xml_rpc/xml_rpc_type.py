from enum import IntEnum

class XmlRpcType(IntEnum):
	'''All supported types that can be transmitted by XML-RPC'''
	Unknown = -1 # Type is not supported
	Array = 0 # The RPC type is a XmlRpcArrayValue
	Boolean = 1 # The RPC type is a XmlRpcBooleanValue
	Double = 2 # The RPC type is a XmlRpcDoubleValue
	Integer = 3 # The RPC type is a XmlRpcIntegerValue
	String = 4 # The RPC type is a XmlRpcStringValue
	Struct = 5 # The RPC type is a XmlRpcStructValue
	Pose = 6 # The RPC type is a XmlRpcPoseValue
