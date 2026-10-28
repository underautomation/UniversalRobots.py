from __future__ import annotations
import typing
from underautomation.universal_robots.common.i_robot_dashboard import IRobotDashboard
from underautomation.universal_robots.rest.rest_api_version import RestApiVersion
from underautomation.universal_robots.rest.rest_api_response import RestApiResponse
from underautomation.universal_robots.rest.robot_state_action import RobotStateAction
from underautomation.universal_robots.rest.program_state_action import ProgramStateAction
from underautomation.universal_robots.rest.rest_api_response_1 import RestApiResponse1
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from underautomation.universal_robots.rest.program_state_response import ProgramStateResponse
from underautomation.universal_robots.common.robot_modes import RobotModes
from underautomation.universal_robots.common.safety_modes import SafetyModes
from underautomation.universal_robots.dashboard.operational_modes import OperationalModes
from underautomation.universal_robots.dashboard.polyscope_version import PolyscopeVersion
from underautomation.universal_robots.rest.rest_program_info import RestProgramInfo
from UnderAutomation.UniversalRobots.Rest.Internal import RestClientBase as rest_client_base
from UnderAutomation.UniversalRobots.Rest import RestApiVersion as rest_api_version
from UnderAutomation.UniversalRobots.Rest import RobotStateAction as robot_state_action
from UnderAutomation.UniversalRobots.Rest import ProgramStateAction as program_state_action
from UnderAutomation.UniversalRobots.Common import RobotModes as robot_modes
from UnderAutomation.UniversalRobots.Common import SafetyModes as safety_modes
from UnderAutomation.UniversalRobots.Dashboard import OperationalModes as operational_modes

class RestClientBase(URServiceBase, IRobotDashboard):
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
		'''Change the robot's operational state.

		:param action: The state action to perform
		:returns: API response indicating success or failure
		'''
		__r = self._instance.ChangeRobotState(robot_state_action(int(action)))
		return None if __r is None else RestApiResponse(__r)

	def unlock_protective_stop(self) -> RestApiResponse:
		'''Unlock the robot from protective stop state.'''
		__r = self._instance.UnlockProtectiveStop()
		return None if __r is None else RestApiResponse(__r)

	def restart_safety(self) -> RestApiResponse:
		'''Restart the safety system.'''
		__r = self._instance.RestartSafety()
		return None if __r is None else RestApiResponse(__r)

	def power_off(self) -> RestApiResponse:
		'''Power off the robot.'''
		__r = self._instance.PowerOff()
		return None if __r is None else RestApiResponse(__r)

	def power_on(self) -> RestApiResponse:
		'''Power on the robot.'''
		__r = self._instance.PowerOn()
		return None if __r is None else RestApiResponse(__r)

	def brake_release(self) -> RestApiResponse:
		'''Release the robot brakes.'''
		__r = self._instance.BrakeRelease()
		return None if __r is None else RestApiResponse(__r)

	def load_program(self, programName: str) -> RestApiResponse:
		'''Load a program by name.

		:param programName: Name of the program to load (without .urp extension)
		:returns: API response indicating success or failure
		'''
		__r = self._instance.LoadProgram(programName)
		return None if __r is None else RestApiResponse(__r)

	def change_program_state(self, action: ProgramStateAction) -> RestApiResponse:
		'''Change the program state.

		:param action: The program action to perform
		:returns: API response indicating success or failure
		'''
		__r = self._instance.ChangeProgramState(program_state_action(int(action)))
		return None if __r is None else RestApiResponse(__r)

	def play(self) -> RestApiResponse:
		'''Start playing the loaded program.'''
		__r = self._instance.Play()
		return None if __r is None else RestApiResponse(__r)

	def pause(self) -> RestApiResponse:
		'''Pause the running program.'''
		__r = self._instance.Pause()
		return None if __r is None else RestApiResponse(__r)

	def stop(self) -> RestApiResponse:
		'''Stop the running program.'''
		__r = self._instance.Stop()
		return None if __r is None else RestApiResponse(__r)

	def resume(self) -> RestApiResponse:
		'''Resume a paused program.'''
		__r = self._instance.Resume()
		return None if __r is None else RestApiResponse(__r)

	def get_program_state(self) -> RestApiResponse1[ProgramStateResponse]:
		'''Get the current program state.

		:returns: API response with the current program state
		'''
		__r = self._instance.GetProgramState()
		return None if __r is None else RestApiResponse1[ProgramStateResponse](None, __r)

	def get_loaded_program(self) -> RestApiResponse1[str]:
		'''Get the name of the loaded program.

		:returns: API response with the name of the loaded program in Value
		'''
		__r = self._instance.GetLoadedProgram()
		return None if __r is None else RestApiResponse1[str](None, __r)

	def get_robot_mode(self) -> RestApiResponse1[RobotModes]:
		'''Get the mode of the robot.

		:returns: API response with the robot mode in Value. A mode that the SDK does not know gives Unknown.
		'''
		__r = self._instance.GetRobotMode()
		return None if __r is None else RestApiResponse1[RobotModes](None, __r)

	def get_safety_mode(self) -> RestApiResponse1[SafetyModes]:
		'''Get the safety mode of the robot.

		:returns: API response with the safety mode in Value. A mode that the SDK does not know gives Unknown.
		'''
		__r = self._instance.GetSafetyMode()
		return None if __r is None else RestApiResponse1[SafetyModes](None, __r)

	def get_operational_mode(self) -> RestApiResponse1[OperationalModes]:
		'''Get the operational mode of the robot.

		:returns: API response with the operational mode in Value. Succeed is false if the mode is not known.
		'''
		__r = self._instance.GetOperationalMode()
		return None if __r is None else RestApiResponse1[OperationalModes](None, __r)

	def is_in_remote_control(self) -> RestApiResponse1[bool]:
		'''Indicate whether the robot is in remote control.

		:returns: API response with true in Value if the robot is in remote control
		'''
		__r = self._instance.IsInRemoteControl()
		return None if __r is None else RestApiResponse1[bool](None, __r)

	def get_polyscope_version(self) -> RestApiResponse1[PolyscopeVersion]:
		'''Get the version of PolyScope X.

		:returns: API response with the version in Value. The Description is the version text of the robot.
		'''
		__r = self._instance.GetPolyscopeVersion()
		return None if __r is None else RestApiResponse1[PolyscopeVersion](None, __r)

	def show_popup(self, message: str) -> RestApiResponse:
		'''Show a popup on the screen of the robot, with an empty title.

		:param message: Text of the popup
		:returns: API response indicating success or failure
		'''
		__r = self._instance.ShowPopup(message)
		return None if __r is None else RestApiResponse(__r)

	def show_popup_with_title(self, title: str, message: str) -> RestApiResponse:
		'''Show a popup on the screen of the robot.

		:param title: Title of the popup
		:param message: Text of the popup
		:returns: API response indicating success or failure
		'''
		__r = self._instance.ShowPopupWithTitle(title, message)
		return None if __r is None else RestApiResponse(__r)

	def close_popup(self) -> RestApiResponse:
		'''Close the popup of the screen of the robot.

		:returns: API response indicating success or failure
		'''
		__r = self._instance.ClosePopup()
		return None if __r is None else RestApiResponse(__r)

	def close_safety_popup(self) -> RestApiResponse:
		'''Close a safety popup of the screen of the robot.

		:returns: API response indicating success or failure
		'''
		__r = self._instance.CloseSafetyPopup()
		return None if __r is None else RestApiResponse(__r)

	def get_programs(self) -> RestApiResponse1[typing.List[RestProgramInfo]]:
		'''List the programs stored on the robot.

		:returns: API response with the programs in Value
		'''
		__r = self._instance.GetPrograms()
		return None if __r is None else RestApiResponse1[typing.List[RestProgramInfo]](None, __r)

	def upload_program_file(self, filePath: str) -> RestApiResponse1[str]:
		'''Upload a new program file to the robot. The robot refuses a program that already exists: use update_program_file() to replace it.

		:param filePath: Path of the program file on this computer
		:returns: API response with the name given by the robot to the program in Value
		'''
		__r = self._instance.UploadProgramFile(filePath)
		return None if __r is None else RestApiResponse1[str](None, __r)

	def upload_program_content(self, fileName: str, content: str) -> RestApiResponse1[str]:
		'''Upload a new program to the robot from its text content. The robot refuses a program that already exists: use update_program_content() to replace it.

		:param fileName: File name of the program
		:param content: Text content of the program file
		:returns: API response with the name given by the robot to the program in Value
		'''
		__r = self._instance.UploadProgramContent(fileName, content)
		return None if __r is None else RestApiResponse1[str](None, __r)

	def update_program_file(self, filePath: str) -> RestApiResponse1[str]:
		'''Replace a program of the robot with a program file.

		:param filePath: Path of the program file on this computer
		:returns: API response with the name of the program in Value
		'''
		__r = self._instance.UpdateProgramFile(filePath)
		return None if __r is None else RestApiResponse1[str](None, __r)

	def update_program_content(self, fileName: str, content: str) -> RestApiResponse1[str]:
		'''Replace a program of the robot from its text content.

		:param fileName: File name of the program
		:param content: Text content of the program file
		:returns: API response with the name of the program in Value
		'''
		__r = self._instance.UpdateProgramContent(fileName, content)
		return None if __r is None else RestApiResponse1[str](None, __r)

	def download_program(self, programName: str) -> RestApiResponse1[str]:
		'''Download a program from the robot.

		:param programName: Name of the program
		:returns: API response with the text content of the program in Value
		'''
		__r = self._instance.DownloadProgram(programName)
		return None if __r is None else RestApiResponse1[str](None, __r)

	def download_program_to_file(self, programName: str, savePath: str) -> RestApiResponse:
		'''Download a program from the robot and save it in a file of this computer.

		:param programName: Name of the program
		:param savePath: Path of the file to write. An existing file is replaced.
		:returns: API response indicating success or failure
		'''
		__r = self._instance.DownloadProgramToFile(programName, savePath)
		return None if __r is None else RestApiResponse(__r)

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
