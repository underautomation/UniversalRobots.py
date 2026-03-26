import typing
from __future__ import annotation
from underautomation.universal_robots.rest.rest_api_version import RestApiVersion
from underautomation.universal_robots.rest.internal.rest_client_base import RestClientBase
from UnderAutomation.UniversalRobots.Internal import RestClientInternal as rest_client_internal
from UnderAutomation.UniversalRobots.Rest import RestApiVersion as rest_api_version

class RestClientInternal(RestClientBase):
	'''Internal REST client for use within the UR class'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rest_client_internal()
		else:
			self._instance = _internal

	def enable(self, port: int=80, version: RestApiVersion=RestApiVersion.V1, timeoutMs: int=5000) -> None:
		'''Enable REST client connection using the IP from the parent UR instance

		:param port: HTTP port for REST API. Default: 80
		:param version: REST API version to use. Default: Latest
		:param timeoutMs: Request timeout in milliseconds. Default: 5000ms
		'''
		self._instance.Enable(port, rest_api_version(int(version)), timeoutMs)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RestClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
