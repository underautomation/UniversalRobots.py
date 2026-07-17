from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.rtde_types import RtdeTypes
from UnderAutomation.UniversalRobots.Rtde import RtdeDataDescription as rtde_data_description_1
from UnderAutomation.UniversalRobots.Rtde import RtdeTypes as rtde_types

T = typing.TypeVar('T')
class RtdeDataDescription1(typing.Generic[T]):
	'''Abstract base class that describes a single RTDE variable, including its name, data type, and array layout.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_data_description_1()
		else:
			self._instance = _internal

	@property
	def data(self) -> T:
		'''Gets the enum value identifying the RTDE variable.'''
		return self._instance.Data

	@property
	def type(self) -> RtdeTypes:
		'''Gets the RTDE wire type of this variable.'''
		return RtdeTypes(int(self._instance.Type))

	@property
	def name(self) -> str:
		'''Gets the protocol name of this variable as defined in the UR RTDE specification.'''
		return self._instance.Name

	@property
	def description(self) -> str:
		'''Gets a human-readable description of this variable.'''
		return self._instance.Description

	@property
	def lower_index(self) -> int:
		'''Gets the lower bound index when this variable represents an element of a register array; otherwise 0.'''
		return self._instance.LowerIndex

	@property
	def array_size(self) -> int:
		'''Gets the size of the register array this variable belongs to; otherwise 0.'''
		return self._instance.ArraySize

	@property
	def is_array(self) -> bool:
		'''Gets a value indicating whether this variable is an element of a register array.'''
		return self._instance.IsArray

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeDataDescription1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
