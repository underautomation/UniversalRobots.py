from __future__ import annotations
import typing
from underautomation.universal_robots.files.ur_archive import URArchive
from UnderAutomation.UniversalRobots.Files import URInstallation as ur_installation

class URInstallation(URArchive):
	'''Functions to encode and decode a *.installation file'''
	def __init__(self, xml: typing.Any, _internal = 0):
		'''Creates a URInstallation from its XML definition.

		:param xml: The XML element representing the installation content.
		'''
		if(_internal == 0):
			self._instance = ur_installation(xml)
		else:
			self._instance = _internal

	@staticmethod
	def load(urpFile: str) -> 'URInstallation':
		'''Load a *.installation file from path'''
		return URInstallation(None, ur_installation.Load(urpFile))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, URInstallation):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# File extension for UR installation files.
URInstallation.EXTENSION = ur_installation.EXTENSION
