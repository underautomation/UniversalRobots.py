import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Ssh.Tools.Common import ObjectIdentifier as object_identifier

class ObjectIdentifier:
	'''Describes object identifier for DER encoding'''
	def __init__(self, identifiers: typing.List[int], _internal = 0):
		'''Initializes a new instance of the ObjectIdentifier class.

		:param identifiers: The identifiers.
		'''
		if(_internal == 0):
			self._instance = object_identifier(identifiers)
		else:
			self._instance = _internal

	@property
	def identifiers(self) -> typing.List[int]:
		'''Gets the object identifier.'''
		return self._instance.Identifiers

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ObjectIdentifier):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
