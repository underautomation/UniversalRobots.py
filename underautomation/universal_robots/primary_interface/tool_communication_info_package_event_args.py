from __future__ import annotations
import typing
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import ToolCommunicationInfoPackageEventArgs as tool_communication_info_package_event_args

class ToolCommunicationInfoPackageEventArgs(PackageEventArgs):
	'''Tool communication info'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tool_communication_info_package_event_args()
		else:
			self._instance = _internal

	@property
	def tool_communication_is_enabled(self) -> bool:
		'''Is the tool communication interface enabled'''
		return self._instance.ToolCommunicationIsEnabled

	@tool_communication_is_enabled.setter
	def tool_communication_is_enabled(self, value: bool):
		self._instance.ToolCommunicationIsEnabled = value

	@property
	def baud_rate(self) -> int:
		'''Baud rate for tool serial communication'''
		return self._instance.BaudRate

	@baud_rate.setter
	def baud_rate(self, value: int):
		self._instance.BaudRate = value

	@property
	def parity(self) -> int:
		'''Parity'''
		return self._instance.Parity

	@parity.setter
	def parity(self, value: int):
		self._instance.Parity = value

	@property
	def stop_bits(self) -> int:
		'''Stop bits'''
		return self._instance.StopBits

	@stop_bits.setter
	def stop_bits(self, value: int):
		self._instance.StopBits = value

	@property
	def rx_idle_chars(self) -> float:
		'''RX Idle Chars'''
		return self._instance.RxIdleChars

	@rx_idle_chars.setter
	def rx_idle_chars(self, value: float):
		self._instance.RxIdleChars = value

	@property
	def tx_idle_chars(self) -> float:
		'''TX Idle Chars'''
		return self._instance.TxIdleChars

	@tx_idle_chars.setter
	def tx_idle_chars(self, value: float):
		self._instance.TxIdleChars = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ToolCommunicationInfoPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
