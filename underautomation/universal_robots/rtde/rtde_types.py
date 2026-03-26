from enum import IntEnum

class RtdeTypes(IntEnum):
	'''RTDE data types used to describe the wire format of each RTDE variable.'''
	Bool = 0 # Boolean value (1 byte on the wire).
	Uint8 = 1 # Unsigned 8-bit integer.
	Uint32 = 2 # Unsigned 32-bit integer.
	Int32 = 3 # Signed 32-bit integer.
	Uint64 = 4 # Unsigned 64-bit integer.
	Double = 5 # 64-bit floating-point number.
	Vector3D = 6 # 3-element double vector (X, Y, Z).
	Pose = 7 # 6-element double vector representing a TCP pose (X, Y, Z, Rx, Ry, Rz).
	CartesianCoordinates = 8 # 6-element double vector representing Cartesian coordinates.
	JointsDoubleValues = 9 # 6-element double vector with one value per robot joint.
	JointsIntValues = 10 # 6-element 32-bit integer vector with one value per robot joint.
	BoolArray = 11 # Boolean value stored as part of a register array.
	Int32Array = 12 # 32-bit integer value stored as part of a register array.
	DoubleArray = 13 # 64-bit double value stored as part of a register array.
