import typing
from __future__ import annotation
from underautomation.universal_robots.rest.rest_api_version import RestApiVersion
from underautomation.universal_robots.rest.rest_api_response import RestApiResponse
from underautomation.universal_robots.rest.robot_state_action import RobotStateAction
from underautomation.universal_robots.rest.program_state_action import ProgramStateAction
from underautomation.universal_robots.rest.rest_api_response_1 import RestApiResponse1
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from underautomation.universal_robots.rest.program_state_response import ProgramStateResponse
from UnderAutomation.UniversalRobots.Rest.Internal import RestClientBase as rest_client_base
from UnderAutomation.UniversalRobots.Rest import RestApiVersion as rest_api_version
from UnderAutomation.UniversalRobots.Rest import RobotStateAction as robot_state_action
from UnderAutomation.UniversalRobots.Rest import ProgramStateAction as program_state_action

class RestClientBase(URServiceBase):
	'''Base implementation of the REST API client for PolyscopeX robots'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rest_client_base()
		else:
			self._instance = _internal

	def disable(self) -> None:
		'''Disable the REST client'''
		self._instance.Disable()

	def change_robot_state(self, action: RobotStateAction) -> RestApiResponse:
		'''Change the robot's operational state. PUT /robotstate/v1/state

		:param action: The state action to perform
		:returns: API response indicating success or failure
		'''
		return RestApiResponse(self._instance.ChangeRobotState(robot_state_action(int(action))))

	def unlock_protective_stop(self) -> RestApiResponse:
		'''Unlock the robot from protective stop state.'''
		return RestApiResponse(self._instance.UnlockProtectiveStop())

	def restart_safety(self) -> RestApiResponse:
		'''Restart the safety system.'''
		return RestApiResponse(self._instance.RestartSafety())

	def power_off(self) -> RestApiResponse:
		'''Power off the robot.'''
		return RestApiResponse(self._instance.PowerOff())

	def power_on(self) -> RestApiResponse:
		'''Power on the robot.'''
		return RestApiResponse(self._instance.PowerOn())

	def brake_release(self) -> RestApiResponse:
		'''Release the robot brakes.'''
		return RestApiResponse(self._instance.BrakeRelease())

	def load_program(self, programName: str) -> RestApiResponse:
		'''Load a program by name. PUT /program/v1/load

		:param programName: Name of the program to load (without .urp extension)
		:returns: API response indicating success or failure
		'''
		return RestApiResponse(self._instance.LoadProgram(programName))

	def change_program_state(self, action: ProgramStateAction) -> RestApiResponse:
		'''Change the program state. PUT /program/v1/state

		:param action: The program action to perform
		:returns: API response indicating success or failure
		'''
		return RestApiResponse(self._instance.ChangeProgramState(program_state_action(int(action))))

	def play(self) -> RestApiResponse:
		'''Start playing the loaded program.'''
		return RestApiResponse(self._instance.Play())

	def pause(self) -> RestApiResponse:
		'''Pause the running program.'''
		return RestApiResponse(self._instance.Pause())

	def stop(self) -> RestApiResponse:
		'''Stop the running program.'''
		return RestApiResponse(self._instance.Stop())

	def resume(self) -> RestApiResponse:
		'''Resume a paused program.'''
		return RestApiResponse(self._instance.Resume())

	def get_program_state(self) -> RestApiResponse1[ProgramStateResponse]:
		'''Get the current program state. GET /program/v1/state

		:returns: API response with the current program state
		'''
		return RestApiResponse1[ProgramStateResponse](None, self._instance.GetProgramState())

	@property
	def ip(self) -> str:
		'''IP address of the robot'''
		return self._instance.IP

	@property
	def port(self) -> int:
		'''HTTP port for REST API'''
		return self._instance.Port

	@property
	def version(self) -> RestApiVersion:
		'''REST API version being used'''
		return RestApiVersion(int(self._instance.Version))

	@property
	def timeout_ms(self) -> int:
		'''Request timeout in milliseconds'''
		return self._instance.TimeoutMs

	@property
	def initialized(self) -> bool:
		'''Indicates whether the REST client has been initialized'''
		return self._instance.Initialized

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RestClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
