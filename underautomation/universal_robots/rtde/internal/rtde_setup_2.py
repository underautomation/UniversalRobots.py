from __future__ import annotations
import typing
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

	@typing.overload
	def add(self, data: U, index: int=0) -> T: ...

	@typing.overload
	def add(self, data: U) -> T: ...

	def add(self, *args, **kwargs) -> T:
		'''Adds a variable to the recipe with the specified register index.
		Adds a variable to the recipe with register index 0.

		Arguments: (data, index)
		Arguments: (data)
		:param data: The RTDE variable to add.
		:param index: Register index for array/register variables.
		:returns: The created setup item.
		'''
		__a = _bind_overload(args, kwargs, ['data', 'index'], {'index': 0})
		if __a is not None:
			data, index = __a
			return self._instance.Add(data, index)
		__a = _bind_overload(args, kwargs, ['data'], {})
		if __a is not None:
			data, = __a
			return self._instance.Add(data)
		raise TypeError("add(): no overload takes these arguments")

	def remove(self, data: U, index: int=-1) -> int:
		'''Removes all items matching the specified variable and optionally a specific register index.

		:param data: The RTDE variable to remove.
		:param index: If non-negative, only items with this index are removed; if negative, all matching items are removed.
		:returns: The number of items removed.
		'''
		return self._instance.Remove(data, index)

	@typing.overload
	def contains(self, data: U, index: int=0) -> bool: ...

	@typing.overload
	def contains(self, data: U) -> bool: ...

	def contains(self, *args, **kwargs) -> bool:
		'''Determines whether the recipe contains the specified variable at the given register index.
		Determines whether the recipe contains the specified variable at any register index.

		Arguments: (data, index)
		Arguments: (data)
		:param data: The RTDE variable to look for.
		:param index: Register index to match.
		:returns: true if found; otherwise false.
		'''
		__a = _bind_overload(args, kwargs, ['data', 'index'], {'index': 0})
		if __a is not None:
			data, index = __a
			return self._instance.Contains(data, index)
		__a = _bind_overload(args, kwargs, ['data'], {})
		if __a is not None:
			data, = __a
			return self._instance.Contains(data)
		raise TypeError("contains(): no overload takes these arguments")

	def to_distinct_list(self) -> typing.List[T]:
		'''Returns a deduplicated array of setup items, removing duplicates by data and index.

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

def _bind_overload(args, kwargs, names, defaults):
	if len(args) > len(names) or any(k not in names[len(args):] for k in kwargs):
		return None
	values = list(args)
	for name in names[len(args):]:
		if name in kwargs:
			values.append(kwargs[name])
		elif name in defaults:
			values.append(defaults[name])
		else:
			return None
	return values
