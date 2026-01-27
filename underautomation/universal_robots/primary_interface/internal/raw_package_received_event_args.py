import typing
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.PrimaryInterface.Internal import RawPackageReceivedEventArgs as raw_package_received_event_args

class RawPackageReceivedEventArgs(PackageEventArgs):
	def __init__(self, data: typing.List[int], receiveDate: typing.Any, type: int, _internal = 0):
		if(_internal == 0):
			self._instance = raw_package_received_event_args(data, receiveDate, type)
		else:
			self._instance = _internal
	@property
	def data(self) -> typing.List[int]:
		return self._instance.Data
	@property
	def type(self) -> int:
		return self._instance.Type
