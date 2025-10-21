import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Ssh.Tools import IRemotePathTransformation as i_remote_path_transformation

class IRemotePathTransformation:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_remote_path_transformation()
		else:
			self._instance = _internal
	def transform(self, path: str) -> str:
		return self._instance.Transform(path)
