import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.XmlRpc import XmlRpcType as xml_rpc_type

class XmlRpcType(int):
	Unknown = xml_rpc_type.Unknown
	Array = xml_rpc_type.Array
	Boolean = xml_rpc_type.Boolean
	Double = xml_rpc_type.Double
	Integer = xml_rpc_type.Integer
	String = xml_rpc_type.String
	Struct = xml_rpc_type.Struct
	Pose = xml_rpc_type.Pose
