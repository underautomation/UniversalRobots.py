from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.rtde_output_setup import RtdeOutputSetup
from underautomation.universal_robots.rtde.rtde_input_setup import RtdeInputSetup
from underautomation.universal_robots.rtde.rtde_versions import RtdeVersions
from underautomation.universal_robots.rtde.internal.rtde_client_base import RtdeClientBase
from UnderAutomation.UniversalRobots.Internal import RtdeClientInternal as rtde_client_internal
from UnderAutomation.UniversalRobots.Rtde import RtdeVersions as rtde_versions

class RtdeClientInternal(RtdeClientBase):
	'''Internal implementation of the Real-Time Data Exchange (RTDE) client that delegates connection to the parent UR instance.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_client_internal()
		else:
			self._instance = _internal

	def connect(self, outputSetup: RtdeOutputSetup, inputSetup: RtdeInputSetup, version: RtdeVersions, frequency: float, port: int) -> None:
		'''Connects to the RTDE interface on the robot controller.

		:param outputSetup: Configuration for RTDE output subscriptions.
		:param inputSetup: Configuration for RTDE input registers.
		:param version: RTDE protocol version to negotiate.
		:param frequency: Output data frequency in Hz.
		:param port: TCP port of the RTDE server.
		'''
		self._instance.Connect(outputSetup._instance if outputSetup else None, inputSetup._instance if inputSetup else None, rtde_versions(int(version)), frequency, port)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
