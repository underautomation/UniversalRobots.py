from __future__ import annotations
import typing
from underautomation.universal_robots.primary_interface.requested_types import RequestedTypes
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import RequestValueMessageEventArgs as request_value_message_event_args
from UnderAutomation.UniversalRobots.PrimaryInterface import RequestedTypes as requested_types

class RequestValueMessageEventArgs(PackageEventArgs):
	'''Event data for a request value message received from the robot (assignment popup requesting user input).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = request_value_message_event_args()
		else:
			self._instance = _internal

	@property
	def request_id(self) -> int:
		'''Unique identifier of the request.'''
		return self._instance.RequestId

	@request_id.setter
	def request_id(self, value: int):
		self._instance.RequestId = value

	@property
	def requested_type(self) -> RequestedTypes:
		'''Data type requested from the user.'''
		return RequestedTypes(int(self._instance.RequestedType))

	@requested_type.setter
	def requested_type(self, value: RequestedTypes):
		self._instance.RequestedType = requested_types(int(value))

	@property
	def request_text_message(self) -> str:
		'''Message displayed to the user in the request popup.'''
		return self._instance.RequestTextMessage

	@request_text_message.setter
	def request_text_message(self, value: str):
		self._instance.RequestTextMessage = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RequestValueMessageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
