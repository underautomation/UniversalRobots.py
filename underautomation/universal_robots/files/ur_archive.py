import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Files import URArchive as ur_archive

class URArchive:
	'''Contains basic methods to encode and decode a UR archive'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ur_archive()
		else:
			self._instance = _internal

	def save(self, directory: str) -> str:
		'''Save encoded file to a directory, overwrite it if it exists

		:param directory: Directory to save the file
		:returns: Full name of the saved file
		'''
		return self._instance.Save(directory)

	@staticmethod
	def load(fileStream: typing.Any) -> typing.Any:
		'''Load a UR archive from stream and decode it as XML'''
		return ur_archive.Load(fileStream)

	@property
	def xml(self) -> typing.Any:
		'''XML description of the object'''
		return self._instance.XML

	@property
	def name(self) -> str:
		'''Gets or sets the name of this archive, stored as an XML attribute.'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def file_name(self) -> str:
		'''File name that should be used on a UR robot'''
		return self._instance.FileName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, URArchive):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
