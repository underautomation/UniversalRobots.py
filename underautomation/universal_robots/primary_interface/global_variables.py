import typing
from __future__ import annotation
from underautomation.universal_robots.primary_interface.global_variables_firmware_version import GlobalVariablesFirmwareVersion
from underautomation.universal_robots.common.global_variable import GlobalVariable
from underautomation.universal_robots.primary_interface.global_variables_event_args import GlobalVariablesEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import GlobalVariables as global_variables
from UnderAutomation.UniversalRobots.PrimaryInterface import GlobalVariablesFirmwareVersion as global_variables_firmware_version

class GlobalVariables:
	'''List of all global variables'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = global_variables()
		else:
			self._instance = _internal

	def values_updated(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ValuesUpdated+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def list_updated(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ListUpdated+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def get_all(self) -> typing.List[GlobalVariable]:
		'''Returns a list of all variables declared in the robot'''
		return [GlobalVariable(x) for x in self._instance.GetAll()]

	def get_by_name(self, name: str) -> GlobalVariable:
		'''Get a variable by its name. Null is returned if the variable doesn't exist

		:param name: Variable name, not case sensitive
		'''
		return GlobalVariable(self._instance.GetByName(name))

	@property
	def firmware_version(self) -> GlobalVariablesFirmwareVersion:
		'''Indicates which decoder is used used to read variables according to firmware version'''
		return GlobalVariablesFirmwareVersion(int(self._instance.FirmwareVersion))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GlobalVariables):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
