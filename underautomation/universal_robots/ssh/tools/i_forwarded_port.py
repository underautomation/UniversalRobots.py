import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Ssh.Tools import IForwardedPort as i_forwarded_port

class IForwardedPort:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_forwarded_port()
		else:
			self._instance = _internal
	def closing(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.Closing+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))
