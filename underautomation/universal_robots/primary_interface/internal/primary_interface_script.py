from __future__ import annotations
import typing
from underautomation.universal_robots.common.status_code import StatusCode
from UnderAutomation.UniversalRobots.PrimaryInterface.Internal import PrimaryInterfaceScript as primary_interface_script
from UnderAutomation.UniversalRobots.Common import StatusCode as status_code

class PrimaryInterfaceScript:
	'''Handles Primary interface send script feature'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = primary_interface_script()
		else:
			self._instance = _internal

	def send(self, script: str) -> StatusCode:
		'''Remotely execute script.Please see the Universal Robot Script documentation : https://www.universal-robots.com/download/.

		:param script: The script command to execute. You can for example move the robot at a specified joint coordinate with the command : movej([-1.5,-1.5,-2,-0.5,1.8,0],a=1.4, v=1.05, t=0, r=0)
		'''
		return StatusCode(int(self._instance.Send(script)))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PrimaryInterfaceScript):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
