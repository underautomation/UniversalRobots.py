import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Dashboard.Internal import DashboardClientParametersBase as dashboard_client_parameters_base

class DashboardClientParametersBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dashboard_client_parameters_base()
		else:
			self._instance = _internal
	@property
	def port(self) -> int:
		return self._instance.Port
	@port.setter
	def port(self, value: int):
		self._instance.Port = value
	@property
	def defaul_t__port(self) -> int:
		return self._instance.DEFAULT_PORT
	@defaul_t__port.setter
	def defaul_t__port(self, value: int):
		self._instance.DEFAULT_PORT = value
