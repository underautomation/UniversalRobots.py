import typing
from __future__ import annotation
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import CalibrationDataPackageEventArgs as calibration_data_package_event_args

class CalibrationDataPackageEventArgs(PackageEventArgs):
	'''Calibration data'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = calibration_data_package_event_args()
		else:
			self._instance = _internal

	@property
	def fx(self) -> float:
		'''Fx calibration data'''
		return self._instance.Fx

	@fx.setter
	def fx(self, value: float):
		self._instance.Fx = value

	@property
	def fy(self) -> float:
		'''Fy calibration data'''
		return self._instance.Fy

	@fy.setter
	def fy(self, value: float):
		self._instance.Fy = value

	@property
	def fz(self) -> float:
		'''Fz calibration data'''
		return self._instance.Fz

	@fz.setter
	def fz(self, value: float):
		self._instance.Fz = value

	@property
	def frx(self) -> float:
		'''Frx calibration data'''
		return self._instance.Frx

	@frx.setter
	def frx(self, value: float):
		self._instance.Frx = value

	@property
	def fry(self) -> float:
		'''Fry calibration data'''
		return self._instance.Fry

	@fry.setter
	def fry(self, value: float):
		self._instance.Fry = value

	@property
	def frz(self) -> float:
		'''Frz calibration data'''
		return self._instance.Frz

	@frz.setter
	def frz(self, value: float):
		self._instance.Frz = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CalibrationDataPackageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
