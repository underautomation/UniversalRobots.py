import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import ConnectException as connect_exception

class ConnectException:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = connect_exception()
		else:
			self._instance = _internal
	@property
	def service(self) -> str:
		return self._instance.Service
	@property
	def robot_ip(self) -> str:
		return self._instance.RobotIp
