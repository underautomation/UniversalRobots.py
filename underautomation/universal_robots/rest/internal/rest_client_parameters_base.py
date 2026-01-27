import typing
from underautomation.universal_robots.rest.rest_api_version import RestApiVersion
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rest.Internal import RestClientParametersBase as rest_client_parameters_base

class RestClientParametersBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rest_client_parameters_base()
		else:
			self._instance = _internal
	@property
	def port(self) -> int:
		return self._instance.Port
	@port.setter
	def port(self, value: int):
		self._instance.Port = value
	@property
	def version(self) -> RestApiVersion:
		return RestApiVersion(self._instance.Version)
	@version.setter
	def version(self, value: RestApiVersion):
		self._instance.Version = value
	@property
	def timeout_ms(self) -> int:
		return self._instance.TimeoutMs
	@timeout_ms.setter
	def timeout_ms(self, value: int):
		self._instance.TimeoutMs = value

RestClientParametersBase.defaul_t__port = RestClientParametersBase(rest_client_parameters_base.DEFAULT_PORT)

RestClientParametersBase.defaul_t__timeou_t__ms = RestClientParametersBase(rest_client_parameters_base.DEFAULT_TIMEOUT_MS)
