from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.rtde_data_description_1 import RtdeDataDescription1
from underautomation.universal_robots.rtde.rtde_types import RtdeTypes
from UnderAutomation.UniversalRobots.Rtde.Internal import RtdeSetupItem as rtde_setup_item_1
from UnderAutomation.UniversalRobots.Rtde import RtdeTypes as rtde_types

T = typing.TypeVar('T')
class RtdeSetupItem1(typing.Generic[T]):
	'''Abstract base class representing a single RTDE variable in a recipe, identified by an enum value of type T and an optional register index.'''
	def __init__(self, data: T, index: int, _internal = 0):
		'''Initializes a new instance for the specified RTDE variable and register index.

		:param data: The RTDE variable identifier.
		:param index: Register index for array/register variables.
		'''
		if(_internal == 0):
			self._instance = rtde_setup_item_1(data, index)
		else:
			self._instance = _internal

	@property
	def index(self) -> int:
		'''Gets or sets the register index for array/register RTDE variables. Defaults to 0.'''
		return self._instance.Index

	@index.setter
	def index(self, value: int):
		self._instance.Index = value

	@property
	def data(self) -> T:
		'''Gets or sets the enum value identifying the RTDE variable.'''
		return self._instance.Data

	@data.setter
	def data(self, value: T):
		self._instance.Data = value

	@property
	def description(self) -> RtdeDataDescription1[T]:
		'''Gets the description metadata for this variable (name, type, array info).'''
		return RtdeDataDescription1[T](self._instance.Description)

	@property
	def name(self) -> str:
		'''Gets the RTDE protocol name for this variable, including the register index suffix for array variables.'''
		return self._instance.Name

	@property
	def type(self) -> RtdeTypes:
		'''Gets the RTDE wire type of this variable.'''
		return RtdeTypes(int(self._instance.Type))

	@property
	def protocol_type(self) -> str:
		'''Gets the uppercase RTDE protocol type string sent on the wire during setup.'''
		return self._instance.ProtocolType

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeSetupItem1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
