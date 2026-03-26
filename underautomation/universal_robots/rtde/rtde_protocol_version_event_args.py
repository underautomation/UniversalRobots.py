import typing
from __future__ import annotation
from underautomation.universal_robots.rtde.rtde_versions import RtdeVersions
from underautomation.universal_robots.rtde.rtde_basic_request_event_args import RtdeBasicRequestEventArgs
from UnderAutomation.UniversalRobots.Rtde import RtdeProtocolVersionEventArgs as rtde_protocol_version_event_args
from UnderAutomation.UniversalRobots.Rtde import RtdeVersions as rtde_versions

class RtdeProtocolVersionEventArgs(RtdeBasicRequestEventArgs):
	'''Event arguments indicating which RTDE protocol version was negotiated with the robot.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_protocol_version_event_args()
		else:
			self._instance = _internal

	@property
	def version(self) -> RtdeVersions:
		'''Gets or sets the negotiated RTDE protocol version.'''
		return RtdeVersions(int(self._instance.Version))

	@version.setter
	def version(self, value: RtdeVersions):
		self._instance.Version = rtde_versions(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeProtocolVersionEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
