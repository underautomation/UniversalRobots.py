from __future__ import annotations
import typing
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import KeyMessageEventArgs as key_message_event_args

class KeyMessageEventArgs(PackageEventArgs):
	'''Internal robot events (such as starting or stopping a program)'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = key_message_event_args()
		else:
			self._instance = _internal

	@property
	def robot_message_code(self) -> int:
		'''Message code'''
		return self._instance.RobotMessageCode

	@robot_message_code.setter
	def robot_message_code(self, value: int):
		self._instance.RobotMessageCode = value

	@property
	def robot_message_argument(self) -> int:
		'''Message argument'''
		return self._instance.RobotMessageArgument

	@robot_message_argument.setter
	def robot_message_argument(self, value: int):
		self._instance.RobotMessageArgument = value

	@property
	def robot_message_title(self) -> str:
		'''Message title'''
		return self._instance.RobotMessageTitle

	@robot_message_title.setter
	def robot_message_title(self, value: str):
		self._instance.RobotMessageTitle = value

	@property
	def key_text_message(self) -> str:
		'''Message key'''
		return self._instance.KeyTextMessage

	@key_text_message.setter
	def key_text_message(self, value: str):
		self._instance.KeyTextMessage = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, KeyMessageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
