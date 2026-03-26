import typing
from __future__ import annotation
from underautomation.universal_robots.rtde.rtde_output_setup import RtdeOutputSetup
from underautomation.universal_robots.rtde.rtde_input_setup import RtdeInputSetup
from underautomation.universal_robots.rtde.rtde_versions import RtdeVersions
from underautomation.universal_robots.rtde.rtde_outputs_description import RtdeOutputsDescription
from underautomation.universal_robots.rtde.rtde_inputs_description import RtdeInputsDescription
from underautomation.universal_robots.rtde.internal.rtde_client_base import RtdeClientBase
from UnderAutomation.UniversalRobots.Rtde import RtdeClient as rtde_client
from UnderAutomation.UniversalRobots.Rtde import RtdeVersions as rtde_versions

class RtdeClient(RtdeClientBase):
	'''Standalone RTDE client for exchanging real-time data with a Universal Robots controller on TCP port 30004.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, outputSetup: RtdeOutputSetup, inputSetup: RtdeInputSetup, version: RtdeVersions, frequency: float, port: int=30004) -> None:
		'''Connects to the robot's RTDE interface, sets up the specified input/output recipes, and starts data streaming.

		:param ip: IP address of the robot.
		:param outputSetup: Output variables to subscribe to (robot-to-client).
		:param inputSetup: Input variables to write (client-to-robot).
		:param version: Preferred RTDE protocol version.
		:param frequency: Desired output data frequency in Hz (RTDE v2 only).
		:param port: TCP port. Default is 30004.
		'''
		self._instance.Connect(ip, outputSetup._instance if outputSetup else None, inputSetup._instance if inputSetup else None, rtde_versions(int(version)), frequency, port)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Static description of all available RTDE output variables.
RtdeClient.AllOutputsDescription = RtdeOutputsDescription(rtde_client.AllOutputsDescription)

# Static description of all available RTDE input variables.
RtdeClient.AllInputsDescription = RtdeInputsDescription(rtde_client.AllInputsDescription)
