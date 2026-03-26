import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.PrimaryInterface import JointKinematicsInfo as joint_kinematics_info

class JointKinematicsInfo:
	'''Joint kinematics info, Denavit–Hartenberg (DH) parameters'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_kinematics_info()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def checksum(self) -> int:
		'''Joint checksum'''
		return self._instance.Checksum

	@checksum.setter
	def checksum(self, value: int):
		self._instance.Checksum = value

	@property
	def d_htheta(self) -> float:
		'''DH convention theta parameter'''
		return self._instance.DHtheta

	@d_htheta.setter
	def d_htheta(self, value: float):
		self._instance.DHtheta = value

	@property
	def d_ha(self) -> float:
		'''DH convention a parameter'''
		return self._instance.DHa

	@d_ha.setter
	def d_ha(self, value: float):
		self._instance.DHa = value

	@property
	def d_hd(self) -> float:
		'''DH convention d parameter'''
		return self._instance.DHd

	@d_hd.setter
	def d_hd(self, value: float):
		self._instance.DHd = value

	@property
	def dhalpha(self) -> float:
		'''DH convention alpha parameter'''
		return self._instance.Dhalpha

	@dhalpha.setter
	def dhalpha(self, value: float):
		self._instance.Dhalpha = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointKinematicsInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
