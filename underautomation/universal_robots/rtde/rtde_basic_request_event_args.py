import typing
from __future__ import annotation
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.Rtde import RtdeBasicRequestEventArgs as rtde_basic_request_event_args

class RtdeBasicRequestEventArgs(PackageEventArgs):
	'''Event arguments for a basic RTDE request/response exchange indicating whether the request was accepted by the robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_basic_request_event_args()
		else:
			self._instance = _internal

	@property
	def accepted(self) -> bool:
		'''Gets or sets a value indicating whether the request was accepted by the robot.'''
		return self._instance.Accepted

	@accepted.setter
	def accepted(self, value: bool):
		self._instance.Accepted = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeBasicRequestEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
