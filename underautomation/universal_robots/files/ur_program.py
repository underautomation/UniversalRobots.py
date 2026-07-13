from __future__ import annotations
import typing
from underautomation.universal_robots.files.ur_archive import URArchive
from UnderAutomation.UniversalRobots.Files import URProgram as ur_program

class URProgram(URArchive):
	'''Functions to compile and decompile a *.urp program file'''
	def __init__(self, xml: typing.Any, _internal = 0):
		'''Creates a URProgram from its XML definition.

		:param xml: The XML element representing the program content.
		'''
		if(_internal == 0):
			self._instance = ur_program(xml)
		else:
			self._instance = _internal

	@staticmethod
	def load(urpFile: str) -> 'URProgram':
		'''Load a *.urp program from file path'''
		return URProgram(None, ur_program.Load(urpFile))

	def equals(self, obj: typing.Any) -> bool:
		'''Determines whether the specified object is equal to this program.'''
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		'''Returns a hash code for this program.'''
		return self._instance.GetHashCode()

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, URProgram):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# File extension for UR program files.
URProgram.EXTENSION = ur_program.EXTENSION
