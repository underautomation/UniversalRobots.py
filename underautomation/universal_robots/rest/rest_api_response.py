import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rest import RestApiResponse as rest_api_response

class RestApiResponse:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rest_api_response()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def succeed(self) -> bool:
		return self._instance.Succeed
	@succeed.setter
	def succeed(self, value: bool):
		self._instance.Succeed = value
	@property
	def status_code(self) -> typing.Any:
		return self._instance.StatusCode
	@status_code.setter
	def status_code(self, value: typing.Any):
		self._instance.StatusCode = value
	@property
	def message(self) -> str:
		return self._instance.Message
	@message.setter
	def message(self, value: str):
		self._instance.Message = value
	@property
	def raw_response(self) -> str:
		return self._instance.RawResponse
	@raw_response.setter
	def raw_response(self, value: str):
		self._instance.RawResponse = value
