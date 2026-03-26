import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Ssh.Tools import IRemotePathTransformation as i_remote_path_transformation

class IRemotePathTransformation:
	'''Represents a transformation that can be applied to a remote path.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_remote_path_transformation()
		else:
			self._instance = _internal

	def transform(self, path: str) -> str:
		'''Transforms the specified remote path.

		:param path: The path to transform.
		:returns: The transformed path.
		'''
		return self._instance.Transform(path)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IRemotePathTransformation):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
