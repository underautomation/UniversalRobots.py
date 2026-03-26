import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Rest import RestApiResponse as rest_api_response
from System.Net import HttpStatusCode as http_status_code

class RestApiResponse:
	'''Response from a REST API call'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rest_api_response()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def succeed(self) -> bool:
		'''Indicates whether the API call succeeded (HTTP 200)'''
		return self._instance.Succeed

	@succeed.setter
	def succeed(self, value: bool):
		self._instance.Succeed = value

	@property
	def status_code(self) -> typing.Any:
		'''HTTP status code returned by the API'''
		return self._instance.StatusCode

	@status_code.setter
	def status_code(self, value: typing.Any):
		self._instance.StatusCode = http_status_code(int(value))

	@property
	def message(self) -> str:
		'''Response message or error description'''
		return self._instance.Message

	@message.setter
	def message(self, value: str):
		self._instance.Message = value

	@property
	def raw_response(self) -> str:
		'''Raw JSON response body'''
		return self._instance.RawResponse

	@raw_response.setter
	def raw_response(self, value: str):
		self._instance.RawResponse = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RestApiResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
