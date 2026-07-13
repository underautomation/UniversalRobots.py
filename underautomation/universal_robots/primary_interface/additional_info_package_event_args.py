from __future__ import annotations
import typing
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import AdditionalInfoPackageEventArgs as additional_info_package_event_args

class AdditionalInfoPackageEventArgs(PackageEventArgs):
	'''Additional information'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = additional_info_package_event_args()
		else:
			self._instance = _internal

	@property
	def freedrive_button_pressed(self) -> bool:
		'''The free drive button is pressed'''
		return self._instance.FreedriveButtonPressed

	@freedrive_button_pressed.setter
	def freedrive_button_pressed(self, value: bool):
		self._instance.FreedriveButtonPressed = value

	@property
	def freedrive_button_enabled(self) -> bool:
		'''The free drive button is enabled'''
		return self._instance.FreedriveButtonEnabled

	@freedrive_button_enabled.setter
	def freedrive_button_enabled(self, value: bool):
		self._instance.FreedriveButtonEnabled = value

	@property
	def io_enabled_freedrive(self) -> bool:
		'''Free drive is enable via IO'''
		return self._instance.IOEnabledFreedrive

	@io_enabled_freedrive.setter
	def io_enabled_freedrive(self, value: bool):
		self._instance.IOEnabledFreedrive = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AdditionalInfoPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
