import typing
from __future__ import annotation
from underautomation.universal_robots.primary_interface.requested_types import RequestedTypes
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import PopupMessageEventArgs as popup_message_event_args
from UnderAutomation.UniversalRobots.PrimaryInterface import RequestedTypes as requested_types

class PopupMessageEventArgs(PackageEventArgs):
	'''Popup message that appears with the Assignment instruction or the URScript popup() function'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = popup_message_event_args()
		else:
			self._instance = _internal

	@property
	def request_id(self) -> int:
		'''Each popup has a unique ID'''
		return self._instance.RequestId

	@request_id.setter
	def request_id(self, value: int):
		self._instance.RequestId = value

	@property
	def requested_type(self) -> RequestedTypes:
		'''Type for assignment popups'''
		return RequestedTypes(int(self._instance.RequestedType))

	@requested_type.setter
	def requested_type(self, value: RequestedTypes):
		self._instance.RequestedType = requested_types(int(value))

	@property
	def warning(self) -> bool:
		'''Popup is a warning'''
		return self._instance.Warning

	@warning.setter
	def warning(self, value: bool):
		self._instance.Warning = value

	@property
	def error(self) -> bool:
		'''Popup is an error'''
		return self._instance.Error

	@error.setter
	def error(self, value: bool):
		self._instance.Error = value

	@property
	def blocking(self) -> bool:
		'''Popup is blocking script execution'''
		return self._instance.Blocking

	@blocking.setter
	def blocking(self, value: bool):
		self._instance.Blocking = value

	@property
	def popup_message_title(self) -> str:
		'''Popup title'''
		return self._instance.PopupMessageTitle

	@popup_message_title.setter
	def popup_message_title(self, value: str):
		self._instance.PopupMessageTitle = value

	@property
	def popup_text_message(self) -> str:
		'''Popup message, null for assignment popups'''
		return self._instance.PopupTextMessage

	@popup_text_message.setter
	def popup_text_message(self, value: str):
		self._instance.PopupTextMessage = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PopupMessageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
