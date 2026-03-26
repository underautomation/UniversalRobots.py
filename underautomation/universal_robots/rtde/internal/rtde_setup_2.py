import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Rtde.Internal import RtdeSetup as rtde_setup_2

T = typing.TypeVar('T')
U = typing.TypeVar('U')
class RtdeSetup2(typing.Generic[T, U]):
	'''Base class for an RTDE recipe, a collection of T setup items that describe which RTDE variables to exchange.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_setup_2()
		else:
			self._instance = _internal

	def add(self, data: U, index: int=0) -> T:
		'''Adds a variable to the recipe with the specified register index.

		:param data: The RTDE variable to add.
		:param index: Register index for array/register variables.
		:returns: The created setup item.
		'''
		return self._instance.Add(data, index)

	def remove(self, data: U, index: int=-1) -> int:
		'''Removes all items matching the specified variable and optionally a specific register index.

		:param data: The RTDE variable to remove.
		:param index: If non-negative, only items with this index are removed; if negative, all matching items are removed.
		:returns: The number of items removed.
		'''
		return self._instance.Remove(data, index)

	def contains(self, data: U, index: int=0) -> bool:
		'''Determines whether the recipe contains the specified variable at the given register index.

		:param data: The RTDE variable to look for.
		:param index: Register index to match.
		:returns: true if found; otherwise false.
		'''
		return self._instance.Contains(data, index)

	def to_distinct_list(self) -> typing.List[T]:
		'''Returns a deduplicated array of setup items, removing duplicates by Data and Index.

		:returns: An array of distinct setup items.
		'''
		return list(self._instance.ToDistinctList())

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeSetup2):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __iter__(self):
		enumerator = self._instance.GetEnumerator()
		while enumerator.MoveNext():
			yield enumerator.Current

	def __len__(self) -> int:
		return self._instance.Count
