import typing
from __future__ import annotation
from underautomation.universal_robots.primary_interface.program_thread import ProgramThread
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import ProgramThreadsEventArgs as program_threads_event_args

class ProgramThreadsEventArgs(PackageEventArgs):
	'''Event data containing information about currently running program threads.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = program_threads_event_args()
		else:
			self._instance = _internal

	@property
	def threads(self) -> typing.List[ProgramThread]:
		'''Array of currently running program threads.'''
		return [ProgramThread(x) for x in self._instance.Threads]

	@threads.setter
	def threads(self, value: typing.List[ProgramThread]):
		self._instance.Threads = [x._instance if x else None for x in value]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ProgramThreadsEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
