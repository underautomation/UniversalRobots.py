import typing
from __future__ import annotation
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.Rtde import RtdeTextMessageEventArgs as rtde_text_message_event_args

class RtdeTextMessageEventArgs(PackageEventArgs):
	'''Event arguments for a text message received from the robot via the RTDE interface.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_text_message_event_args()
		else:
			self._instance = _internal

	@property
	def message(self) -> str:
		'''Gets or sets the text content of the message.'''
		return self._instance.Message

	@message.setter
	def message(self, value: str):
		self._instance.Message = value

	@property
	def source(self) -> str:
		'''Gets or sets the source module that generated the message on the robot.'''
		return self._instance.Source

	@source.setter
	def source(self, value: str):
		self._instance.Source = value

	@property
	def warning_level(self) -> int:
		'''Gets or sets the warning level of the message (0 = exception/error, 1 = warning, 2 = info).'''
		return self._instance.WarningLevel

	@warning_level.setter
	def warning_level(self, value: int):
		self._instance.WarningLevel = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeTextMessageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
