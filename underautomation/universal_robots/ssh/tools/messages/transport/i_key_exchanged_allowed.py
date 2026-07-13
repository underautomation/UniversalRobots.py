from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Ssh.Tools.Messages.Transport import IKeyExchangedAllowed as i_key_exchanged_allowed

class IKeyExchangedAllowed:
	'''Indicates that message that implement this interface is allowed during key exchange phase'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_key_exchanged_allowed()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IKeyExchangedAllowed):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
