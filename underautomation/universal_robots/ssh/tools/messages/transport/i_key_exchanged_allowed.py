import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Ssh.Tools.Messages.Transport import IKeyExchangedAllowed as i_key_exchanged_allowed

class IKeyExchangedAllowed:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_key_exchanged_allowed()
		else:
			self._instance = _internal
