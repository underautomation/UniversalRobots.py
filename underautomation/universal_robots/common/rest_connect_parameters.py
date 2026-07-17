from __future__ import annotations
import typing
from underautomation.universal_robots.rest.internal.rest_client_parameters_base import RestClientParametersBase
from UnderAutomation.UniversalRobots.Common import RestConnectParameters as rest_connect_parameters

class RestConnectParameters(RestClientParametersBase):
	'''Configuration parameters for REST API connection (PolyscopeX only)'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rest_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Enable REST API client communication. Default value is false because REST API is only available on PolyscopeX robots.'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RestConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
