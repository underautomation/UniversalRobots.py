from __future__ import annotations
import typing
from underautomation.universal_robots.dashboard.command_response import CommandResponse
from underautomation.universal_robots.dashboard.command_response_1 import CommandResponse1
from underautomation.universal_robots.dashboard.user_roles import UserRoles
from underautomation.universal_robots.dashboard.operational_modes import OperationalModes
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from underautomation.universal_robots.common.global_variable import GlobalVariable
from underautomation.universal_robots.common.robot_modes import RobotModes
from underautomation.universal_robots.dashboard.program_save_state import ProgramSaveState
from underautomation.universal_robots.dashboard.program_state import ProgramState
from underautomation.universal_robots.dashboard.polyscope_version import PolyscopeVersion
from underautomation.universal_robots.common.safety_status import SafetyStatus
from underautomation.universal_robots.common.robot_models import RobotModels
from UnderAutomation.UniversalRobots.Dashboard.Internal import DashboardClientBase as dashboard_client_base
from UnderAutomation.UniversalRobots.Dashboard import UserRoles as user_roles
from UnderAutomation.UniversalRobots.Dashboard import OperationalModes as operational_modes
from UnderAutomation.UniversalRobots.Common import RobotModes as robot_modes
from UnderAutomation.UniversalRobots.Common import SafetyStatus as safety_status
from UnderAutomation.UniversalRobots.Common import RobotModels as robot_models

class DashboardClientBase(URServiceBase):
	'''Abstract base class providing Dashboard Server command implementations for the Universal Robots controller. Sends text-based commands over TCP and parses responses. A new TCP connection is created for each command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dashboard_client_base()
		else:
			self._instance = _internal

	def disable(self) -> None:
		'''Disable dashboard client'''
		self._instance.Disable()

	def load_program(self, programName: str) -> CommandResponse:
		'''Start loading the specified program. (From FW 1.4) Returns when both program and associated installation has loaded (or failed). The load command fails if the associated installation requires confirmation of safety.The return value in this case will be 'Error while loading program'.

		:param programName: The name of the program to load with its extension .urp
		'''
		return CommandResponse(self._instance.LoadProgram(programName))

	def play(self) -> CommandResponse:
		'''Starts program, if any program is loaded and robot is ready. (From FW 1.4) Returns failure if the program fails to start.'''
		return CommandResponse(self._instance.Play())

	def stop(self) -> CommandResponse:
		'''Stops running program. (From FW 1.4) Returns failure if the program fails to stop'''
		return CommandResponse(self._instance.Stop())

	def pause(self) -> CommandResponse:
		'''Pauses the running program . (From FW 1.4) Returns failure if the program fails to pause'''
		return CommandResponse(self._instance.Pause())

	def send_custom_dashboard_command(self, command: str) -> CommandResponse:
		'''Send a custom command to the Dashboard Server port'''
		return CommandResponse(self._instance.SendCustomDashboardCommand(command))

	def get_variable(self, name: str) -> CommandResponse1[GlobalVariable]:
		'''Get variable value and estimate its type'''
		return CommandResponse1[GlobalVariable](None, self._instance.GetVariable(name))

	def shutdown(self) -> CommandResponse:
		'''Shuts down and turns off robot and controller. Closes the connection. (From FW 1.4)'''
		return CommandResponse(self._instance.Shutdown())

	def is_program_running(self) -> CommandResponse1[bool]:
		'''Returns a True value is a program is running. (From FW 1.6)'''
		return CommandResponse1[bool](None, self._instance.IsProgramRunning())

	def get_robot_mode(self) -> CommandResponse1[RobotModes]:
		'''Returns the current robot state. (From FW 1.6)'''
		return CommandResponse1[RobotModes](None, self._instance.GetRobotMode())

	def get_loaded_program(self) -> CommandResponse1[str]:
		'''Returns the path of the loaded program. If not program is loaded, Value member is null. (From FW 1.6)'''
		return CommandResponse1[str](None, self._instance.GetLoadedProgram())

	def show_popup(self, message: str) -> CommandResponse:
		'''Shows a popup on Polyscope with the specified message. The popup-text will be translated to the selected language, if the text exists in the language file. (From FW 1.6)

		:param message: Message to show
		'''
		return CommandResponse(self._instance.ShowPopup(message))

	def close_popup(self) -> CommandResponse:
		'''Closes the popup (From FW 1.6)'''
		return CommandResponse(self._instance.ClosePopup())

	def add_to_log(self, message: str) -> CommandResponse:
		'''Adds log-message to the Log history. (From FW 1.8.11657)

		:param message: Message to add in logs
		'''
		return CommandResponse(self._instance.AddToLog(message))

	def is_program_saved(self) -> CommandResponse1[ProgramSaveState]:
		'''Returns the save state of the active program and path to loaded program file. (From FW 1.8.11997)'''
		return CommandResponse1[ProgramSaveState](None, self._instance.IsProgramSaved())

	def get_program_state(self) -> CommandResponse1[ProgramState]:
		'''Returns the state of the active program and path to loaded program file, or STOPPED if no program is loaded'''
		return CommandResponse1[ProgramState](None, self._instance.GetProgramState())

	def get_polyscope_version(self) -> CommandResponse1[PolyscopeVersion]:
		'''Returns the version of the Polyscope software (From FW 1.8.14035)'''
		return CommandResponse1[PolyscopeVersion](None, self._instance.GetPolyscopeVersion())

	def set_user_role(self, role: UserRoles) -> CommandResponse:
		'''Controls the available options on the Welcome screen (From FW 1.8.14035 to 3.12.0)

		:param role: Role to set
		'''
		return CommandResponse(self._instance.SetUserRole(user_roles(int(role))))

	def set_operational_mode(self, mode: OperationalModes) -> CommandResponse:
		'''Controls the operational mode. See User manual for details. If this function is called the operational mode cannot be changed from PolyScope, and the user password is disabled. OperationalModes.None is not a valid operational mode. (From FW 5.0.0)

		:param mode: The new operational mode. OperationalModes.None is not a valid operational mode.
		'''
		return CommandResponse(self._instance.SetOperationalMode(operational_modes(int(mode))))

	def clear_operational_mode(self) -> CommandResponse:
		'''The operational mode can again be changed from PolyScope, and the user password is enabled. (From FW 5.0.0)'''
		return CommandResponse(self._instance.ClearOperationalMode())

	def get_operational_mode(self) -> CommandResponse1[OperationalModes]:
		'''Returns the operational mode. (From FW 5.6)'''
		return CommandResponse1[OperationalModes](None, self._instance.GetOperationalMode())

	def is_in_remote_control(self) -> CommandResponse1[bool]:
		'''Returns the remote control status of the robot. If the robot Is In remote control it returns False And If remote control Is disabled Or robot Is in local control it returns false. (From FW 5.6)'''
		return CommandResponse1[bool](None, self._instance.IsInRemoteControl())

	def power_on(self) -> CommandResponse:
		'''Powers on the robot arm. (From FW 3.0)'''
		return CommandResponse(self._instance.PowerOn())

	def power_off(self) -> CommandResponse:
		'''Powers off the robot arm. (From FW 3.0)'''
		return CommandResponse(self._instance.PowerOff())

	def release_brake(self) -> CommandResponse:
		'''Releases the brakes. (From FW 3.0)'''
		return CommandResponse(self._instance.ReleaseBrake())

	def unlock_protective_stop(self) -> CommandResponse:
		'''Closes the current popup and unlocks protective stop. (From FW 3.1)'''
		return CommandResponse(self._instance.UnlockProtectiveStop())

	def close_safety_popup(self) -> CommandResponse:
		'''Closes a safety popup. (From FW 3.1)'''
		return CommandResponse(self._instance.CloseSafetyPopup())

	def load_installation(self, installation: str) -> CommandResponse:
		'''Loads the specified installation file (From FW 3.2.18654)

		:param installation: The installation to load with its extension .installation.
		'''
		return CommandResponse(self._instance.LoadInstallation(installation))

	def restart_safety(self) -> CommandResponse:
		'''Restarts the safety. Used when robot gets a safety fault or violation to restart the safety. After safety has been rebooted the robot will be in Power Off. (From FW 3.7 to 3.12.0 and from 5.1.0)'''
		return CommandResponse(self._instance.RestartSafety())

	def get_safety_status(self) -> CommandResponse1[SafetyStatus]:
		'''Returns the current safety status. (From FW 3.11 to 3.12 and from FW 5.5)'''
		return CommandResponse1[SafetyStatus](None, self._instance.GetSafetyStatus())

	def get_serial_number(self) -> CommandResponse:
		'''Returns serial number of the robot (FW 3.12 and from FW 5.6)'''
		return CommandResponse(self._instance.GetSerialNumber())

	def get_robot_model(self) -> CommandResponse1[RobotModels]:
		'''Returns the robot model (UR3, UR5, UR10, UR16, ...). (FW 3.12 and from FW 5.6)'''
		return CommandResponse1[RobotModels](None, self._instance.GetRobotModel())

	@property
	def ip(self) -> str:
		'''IP of the robot to connect to for sending commands'''
		return self._instance.IP

	@property
	def port(self) -> int:
		'''Dashboard server port'''
		return self._instance.Port

	@property
	def receive_timeout_ms(self) -> int:
		'''Receive timeout in milliseconds'''
		return self._instance.ReceiveTimeoutMs

	@property
	def send_timeout_ms(self) -> int:
		'''Send timeout in milliseconds'''
		return self._instance.SendTimeoutMs

	@property
	def initialized(self) -> bool:
		'''Indicates that the dashboard client has been initialized and is ready to send commands'''
		return self._instance.Initialized

	@property
	def before_shutdown(self) -> typing.Any:
		'''Event raised when function Shutdown is called.'''
		return self._instance.BeforeShutdown

	@before_shutdown.setter
	def before_shutdown(self, value: typing.Any):
		self._instance.BeforeShutdown = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DashboardClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
