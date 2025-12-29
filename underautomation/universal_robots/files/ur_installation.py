import typing
from underautomation.universal_robots.files.ur_archive import URArchive
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Files import URInstallation as ur_installation

class URInstallation(URArchive):
	def __init__(self, xml: typing.Any, _internal = 0):
		if(_internal == 0):
			self._instance = ur_installation(xml)
		else:
			self._instance = _internal
	@staticmethod
	def load(urpFile: str) -> 'URInstallation':
		return URInstallation(None, ur_installation.Load(urpFile))

URInstallation.extension = URInstallation(None, ur_installation.EXTENSION)
