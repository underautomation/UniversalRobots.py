from __future__ import annotations
import typing
from underautomation.universal_robots.rest.rest_api_response import RestApiResponse
from UnderAutomation.UniversalRobots.Rest import RestApiResponse as rest_api_response_1

T = typing.TypeVar('T')
class RestApiResponse1(RestApiResponse, typing.Generic[T]):
	'''Generic response from a REST API call with typed value'''
	def __init__(self, baseResponse: RestApiResponse, _internal = 0):
		'''Creates a new RestApiResponse from a base response'''
		if(_internal == 0):
			self._instance = rest_api_response_1(baseResponse._instance if baseResponse else None)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def value(self) -> T:
		'''Typed value from the response'''
		return self._instance.Value

	@value.setter
	def value(self, value: T):
		self._instance.Value = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RestApiResponse1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
