import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rtde import RtdeTypes as rtde_types

class RtdeTypes(int):
	Bool = rtde_types.Bool
	Uint8 = rtde_types.Uint8
	Uint32 = rtde_types.Uint32
	Int32 = rtde_types.Int32
	Uint64 = rtde_types.Uint64
	Double = rtde_types.Double
	Vector3D = rtde_types.Vector3D
	Pose = rtde_types.Pose
	CartesianCoordinates = rtde_types.CartesianCoordinates
	JointsDoubleValues = rtde_types.JointsDoubleValues
	JointsIntValues = rtde_types.JointsIntValues
	BoolArray = rtde_types.BoolArray
	Int32Array = rtde_types.Int32Array
	DoubleArray = rtde_types.DoubleArray
