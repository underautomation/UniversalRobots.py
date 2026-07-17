from __future__ import annotations
import typing
from datetime import datetime, timedelta
from UnderAutomation.UniversalRobots.Common import PackageEventArgs as package_event_args

class PackageEventArgs:
	'''Base class of all received data packages'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = package_event_args()
		else:
			self._instance = _internal

	@property
	def receive_date(self) -> datetime:
		'''The date the data has been received'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.ReceiveDate.Ticks // 10)

	@receive_date.setter
	def receive_date(self, value: datetime):
		self._instance.ReceiveDate = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
