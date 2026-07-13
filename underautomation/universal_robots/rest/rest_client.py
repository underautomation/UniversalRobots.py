from __future__ import annotations
import typing
from underautomation.universal_robots.rest.rest_api_version import RestApiVersion
from underautomation.universal_robots.rest.internal.rest_client_base import RestClientBase
from UnderAutomation.UniversalRobots.Rest import RestClient as rest_client
from UnderAutomation.UniversalRobots.Rest import RestApiVersion as rest_api_version

class RestClient(RestClientBase):
	'''Standalone REST API client for PolyscopeX robots. Use this class when you want to interact with the REST API independently from the main UR class.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rest_client()
		else:
			self._instance = _internal

	def enable(self, ip: str, port: int=80, version: RestApiVersion=RestApiVersion.V1, timeoutMs: int=5000) -> None:
		'''Enable the REST client with the specified connection parameters.

		:param ip: IP address of the robot
		:param port: HTTP port for REST API. Default: 80
		:param version: REST API version to use. Default: Latest
		:param timeoutMs: Request timeout in milliseconds. Default: 5000ms
		'''
		self._instance.Enable(ip, port, rest_api_version(int(version)), timeoutMs)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RestClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
