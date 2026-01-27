import typing
from underautomation.universal_robots.rest.internal.rest_client_parameters_base import RestClientParametersBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import RestConnectParameters as rest_connect_parameters

class RestConnectParameters(RestClientParametersBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rest_connect_parameters()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value
