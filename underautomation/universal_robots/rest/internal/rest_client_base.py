import typing
from underautomation.universal_robots.rest.rest_api_version import RestApiVersion
from underautomation.universal_robots.rest.rest_api_response import RestApiResponse
from underautomation.universal_robots.rest.robot_state_action import RobotStateAction
from underautomation.universal_robots.rest.program_state_action import ProgramStateAction
from underautomation.universal_robots.rest.rest_api_response_1 import RestApiResponse1
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from underautomation.universal_robots.rest.program_state_response import ProgramStateResponse
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rest.Internal import RestClientBase as rest_client_base

class RestClientBase(URServiceBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rest_client_base()
		else:
			self._instance = _internal
	def disable(self) -> None:
		self._instance.Disable()
	def change_robot_state(self, action: RobotStateAction) -> RestApiResponse:
		return RestApiResponse(self._instance.ChangeRobotState(action))
	def unlock_protective_stop(self) -> RestApiResponse:
		return RestApiResponse(self._instance.UnlockProtectiveStop())
	def restart_safety(self) -> RestApiResponse:
		return RestApiResponse(self._instance.RestartSafety())
	def power_off(self) -> RestApiResponse:
		return RestApiResponse(self._instance.PowerOff())
	def power_on(self) -> RestApiResponse:
		return RestApiResponse(self._instance.PowerOn())
	def brake_release(self) -> RestApiResponse:
		return RestApiResponse(self._instance.BrakeRelease())
	def load_program(self, programName: str) -> RestApiResponse:
		return RestApiResponse(self._instance.LoadProgram(programName))
	def change_program_state(self, action: ProgramStateAction) -> RestApiResponse:
		return RestApiResponse(self._instance.ChangeProgramState(action))
	def play(self) -> RestApiResponse:
		return RestApiResponse(self._instance.Play())
	def pause(self) -> RestApiResponse:
		return RestApiResponse(self._instance.Pause())
	def stop(self) -> RestApiResponse:
		return RestApiResponse(self._instance.Stop())
	def resume(self) -> RestApiResponse:
		return RestApiResponse(self._instance.Resume())
	def get_program_state(self) -> RestApiResponse1[ProgramStateResponse]:
		return RestApiResponse1[ProgramStateResponse](None, self._instance.GetProgramState())
	@property
	def ip(self) -> str:
		return self._instance.IP
	@property
	def port(self) -> int:
		return self._instance.Port
	@property
	def version(self) -> RestApiVersion:
		return RestApiVersion(self._instance.Version)
	@property
	def timeout_ms(self) -> int:
		return self._instance.TimeoutMs
	@property
	def initialized(self) -> bool:
		return self._instance.Initialized
