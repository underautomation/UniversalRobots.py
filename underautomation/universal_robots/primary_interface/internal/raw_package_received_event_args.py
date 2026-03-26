import typing
from __future__ import annotation
from datetime import datetime, timedelta
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface.Internal import RawPackageReceivedEventArgs as raw_package_received_event_args

class RawPackageReceivedEventArgs(PackageEventArgs):
	'''Event args for raw package received'''
	def __init__(self, data: typing.List[int], receiveDate: datetime, type: int, _internal = 0):
		'''Initializes a new instance with the raw packet data, receive timestamp, and package type.

		:param data: Full raw packet bytes including header.
		:param receiveDate: UTC timestamp when the packet was received.
		:param type: Primary Interface package type identifier byte.
		'''
		if(_internal == 0):
			self._instance = raw_package_received_event_args(data, receiveDate, type)
		else:
			self._instance = _internal

	@property
	def data(self) -> typing.List[int]:
		'''Full raw packet data (including header)'''
		return self._instance.Data

	@property
	def type(self) -> int:
		'''Package Type'''
		return self._instance.Type

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RawPackageReceivedEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
