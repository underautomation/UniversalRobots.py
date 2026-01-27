import typing
from underautomation.universal_robots.rest.rest_api_version import RestApiVersion
from underautomation.universal_robots.rest.internal.rest_client_base import RestClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rest import RestClient as rest_client

class RestClient(RestClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rest_client()
		else:
			self._instance = _internal
	def enable(self, ip: str, port: int=80, version: RestApiVersion=RestApiVersion.V1, timeoutMs: int=5000) -> None:
		self._instance.Enable(ip, port, version, timeoutMs)
