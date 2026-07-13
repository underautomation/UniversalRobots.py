from __future__ import annotations
import typing
from underautomation.universal_robots.rest.rest_api_version import RestApiVersion
from UnderAutomation.UniversalRobots.Rest.Internal import RestClientParametersBase as rest_client_parameters_base
from UnderAutomation.UniversalRobots.Rest import RestApiVersion as rest_api_version

class RestClientParametersBase:
	'''Base parameters for REST API client configuration'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rest_client_parameters_base()
		else:
			self._instance = _internal

	@property
	def port(self) -> int:
		'''REST API HTTP port. Default: 80'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	@property
	def version(self) -> RestApiVersion:
		'''REST API version to use. Default: Latest'''
		return RestApiVersion(int(self._instance.Version))

	@version.setter
	def version(self, value: RestApiVersion):
		self._instance.Version = rest_api_version(int(value))

	@property
	def timeout_ms(self) -> int:
		'''Request timeout in milliseconds. Default: 5000ms'''
		return self._instance.TimeoutMs

	@timeout_ms.setter
	def timeout_ms(self, value: int):
		self._instance.TimeoutMs = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RestClientParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default REST API HTTP port
RestClientParametersBase.DEFAULT_PORT = rest_client_parameters_base.DEFAULT_PORT

# Default request timeout in milliseconds
RestClientParametersBase.DEFAULT_TIMEOUT_MS = rest_client_parameters_base.DEFAULT_TIMEOUT_MS
