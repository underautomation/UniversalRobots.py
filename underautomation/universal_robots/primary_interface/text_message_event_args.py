from __future__ import annotations
import typing
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import TextMessageEventArgs as text_message_event_args

class TextMessageEventArgs(PackageEventArgs):
	'''Describes a log message sent with URScript instruction textmsg()'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = text_message_event_args()
		else:
			self._instance = _internal

	@property
	def text_message(self) -> str:
		'''Log message sent with URScript instruction textmsg()'''
		return self._instance.TextMessage

	@text_message.setter
	def text_message(self, value: str):
		self._instance.TextMessage = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TextMessageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
