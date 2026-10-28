from __future__ import annotations
import typing
from underautomation.universal_robots.common.i_robot_dashboard import IRobotDashboard
from underautomation.universal_robots.dashboard.command_response import CommandResponse
from underautomation.universal_robots.dashboard.command_response_1 import CommandResponse1
from underautomation.universal_robots.dashboard.user_roles import UserRoles
from underautomation.universal_robots.dashboard.operational_modes import OperationalModes
from underautomation.universal_robots.dashboard.flight_report_types import FlightReportTypes
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from underautomation.universal_robots.common.global_variable import GlobalVariable
from underautomation.universal_robots.common.robot_modes import RobotModes
from underautomation.universal_robots.dashboard.program_save_state import ProgramSaveState
from underautomation.universal_robots.dashboard.program_state import ProgramState
from underautomation.universal_robots.dashboard.polyscope_version import PolyscopeVersion
from underautomation.universal_robots.common.safety_status import SafetyStatus
from underautomation.universal_robots.common.safety_modes import SafetyModes
from underautomation.universal_robots.common.robot_models import RobotModels
from UnderAutomation.UniversalRobots.Dashboard.Internal import DashboardClientBase as dashboard_client_base
from UnderAutomation.UniversalRobots.Dashboard import UserRoles as user_roles
from UnderAutomation.UniversalRobots.Dashboard import OperationalModes as operational_modes
from UnderAutomation.UniversalRobots.Dashboard import FlightReportTypes as flight_report_types
from UnderAutomation.UniversalRobots.Common import RobotModes as robot_modes
from UnderAutomation.UniversalRobots.Common import SafetyStatus as safety_status
from UnderAutomation.UniversalRobots.Common import SafetyModes as safety_modes
from UnderAutomation.UniversalRobots.Common import RobotModels as robot_models

class DashboardClientBase(URServiceBase, IRobotDashboard):
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
		__r = self._instance.LoadProgram(programName)
		return None if __r is None else CommandResponse(__r)

	def play(self) -> CommandResponse:
		'''Starts program, if any program is loaded and robot is ready. (From FW 1.4) Returns failure if the program fails to start.'''
		__r = self._instance.Play()
		return None if __r is None else CommandResponse(__r)

	def stop(self) -> CommandResponse:
		'''Stops running program. (From FW 1.4) Returns failure if the program fails to stop'''
		__r = self._instance.Stop()
		return None if __r is None else CommandResponse(__r)

	def pause(self) -> CommandResponse:
		'''Pauses the running program . (From FW 1.4) Returns failure if the program fails to pause'''
		__r = self._instance.Pause()
		return None if __r is None else CommandResponse(__r)

	def resume(self) -> CommandResponse:
		'''Resumes the paused program. Only PolyScope X robots know this command: on the other robots, use play() to resume a paused program.

		:returns: The answer of the robot. Succeed is false if the program cannot be resumed.
		'''
		__r = self._instance.Resume()
		return None if __r is None else CommandResponse(__r)

	def send_custom_dashboard_command(self, command: str) -> CommandResponse:
		'''Send a custom command to the Dashboard Server port'''
		__r = self._instance.SendCustomDashboardCommand(command)
		return None if __r is None else CommandResponse(__r)

	def get_variable(self, name: str) -> CommandResponse1[GlobalVariable]:
		'''Get variable value and estimate its type'''
		__r = self._instance.GetVariable(name)
		return None if __r is None else CommandResponse1[GlobalVariable](None, __r)

	def shutdown(self) -> CommandResponse:
		'''Shuts down and turns off robot and controller. Closes the connection. (From FW 1.4)'''
		__r = self._instance.Shutdown()
		return None if __r is None else CommandResponse(__r)

	def is_program_running(self) -> CommandResponse1[bool]:
		'''Returns a True value is a program is running. (From FW 1.6)'''
		__r = self._instance.IsProgramRunning()
		return None if __r is None else CommandResponse1[bool](None, __r)

	def get_robot_mode(self) -> CommandResponse1[RobotModes]:
		'''Returns the current robot state. (From FW 1.6)'''
		__r = self._instance.GetRobotMode()
		return None if __r is None else CommandResponse1[RobotModes](None, __r)

	def get_loaded_program(self) -> CommandResponse1[str]:
		'''Returns the path of the loaded program. If not program is loaded, Value member is null. (From FW 1.6)'''
		__r = self._instance.GetLoadedProgram()
		return None if __r is None else CommandResponse1[str](None, __r)

	def show_popup(self, message: str) -> CommandResponse:
		'''Shows a popup on Polyscope with the specified message. The popup-text will be translated to the selected language, if the text exists in the language file. (From FW 1.6)

		:param message: Message to show
		'''
		__r = self._instance.ShowPopup(message)
		return None if __r is None else CommandResponse(__r)

	def close_popup(self) -> CommandResponse:
		'''Closes the popup (From FW 1.6)'''
		__r = self._instance.ClosePopup()
		return None if __r is None else CommandResponse(__r)

	def add_to_log(self, message: str) -> CommandResponse:
		'''Adds log-message to the Log history. (From FW 1.8.11657)

		:param message: Message to add in logs
		'''
		__r = self._instance.AddToLog(message)
		return None if __r is None else CommandResponse(__r)

	def is_program_saved(self) -> CommandResponse1[ProgramSaveState]:
		'''Returns the save state of the active program and path to loaded program file. (From FW 1.8.11997)'''
		__r = self._instance.IsProgramSaved()
		return None if __r is None else CommandResponse1[ProgramSaveState](None, __r)

	def get_program_state(self) -> CommandResponse1[ProgramState]:
		'''Returns the state of the active program and path to loaded program file, or STOPPED if no program is loaded'''
		__r = self._instance.GetProgramState()
		return None if __r is None else CommandResponse1[ProgramState](None, __r)

	def get_polyscope_version(self) -> CommandResponse1[PolyscopeVersion]:
		'''Returns the version of the Polyscope software (From FW 1.8.14035)'''
		__r = self._instance.GetPolyscopeVersion()
		return None if __r is None else CommandResponse1[PolyscopeVersion](None, __r)

	def set_user_role(self, role: UserRoles) -> CommandResponse:
		'''Controls the available options on the Welcome screen (From FW 1.8.14035 to 3.12.0)

		:param role: Role to set
		'''
		__r = self._instance.SetUserRole(user_roles(int(role)))
		return None if __r is None else CommandResponse(__r)

	def set_operational_mode(self, mode: OperationalModes) -> CommandResponse:
		'''Controls the operational mode. See User manual for details. If this function is called the operational mode cannot be changed from PolyScope, and the user password is disabled. OperationalModes.None is not a valid operational mode. (From FW 5.0.0)

		:param mode: The new operational mode. OperationalModes.None is not a valid operational mode.
		'''
		__r = self._instance.SetOperationalMode(operational_modes(int(mode)))
		return None if __r is None else CommandResponse(__r)

	def clear_operational_mode(self) -> CommandResponse:
		'''The operational mode can again be changed from PolyScope, and the user password is enabled. (From FW 5.0.0)'''
		__r = self._instance.ClearOperationalMode()
		return None if __r is None else CommandResponse(__r)

	def get_operational_mode(self) -> CommandResponse1[OperationalModes]:
		'''Returns the operational mode. (From FW 5.6)'''
		__r = self._instance.GetOperationalMode()
		return None if __r is None else CommandResponse1[OperationalModes](None, __r)

	def is_in_remote_control(self) -> CommandResponse1[bool]:
		'''Returns the remote control status of the robot. If the robot Is In remote control it returns False And If remote control Is disabled Or robot Is in local control it returns false. (From FW 5.6)'''
		__r = self._instance.IsInRemoteControl()
		return None if __r is None else CommandResponse1[bool](None, __r)

	def power_on(self) -> CommandResponse:
		'''Powers on the robot arm. (From FW 3.0)'''
		__r = self._instance.PowerOn()
		return None if __r is None else CommandResponse(__r)

	def power_off(self) -> CommandResponse:
		'''Powers off the robot arm. (From FW 3.0)'''
		__r = self._instance.PowerOff()
		return None if __r is None else CommandResponse(__r)

	def release_brake(self) -> CommandResponse:
		'''Releases the brakes. (From FW 3.0)'''
		__r = self._instance.ReleaseBrake()
		return None if __r is None else CommandResponse(__r)

	def unlock_protective_stop(self) -> CommandResponse:
		'''Closes the current popup and unlocks protective stop. (From FW 3.1)'''
		__r = self._instance.UnlockProtectiveStop()
		return None if __r is None else CommandResponse(__r)

	def close_safety_popup(self) -> CommandResponse:
		'''Closes a safety popup. (From FW 3.1)'''
		__r = self._instance.CloseSafetyPopup()
		return None if __r is None else CommandResponse(__r)

	def load_installation(self, installation: str) -> CommandResponse:
		'''Loads the specified installation file (From FW 3.2.18654)

		:param installation: The installation to load with its extension .installation.
		'''
		__r = self._instance.LoadInstallation(installation)
		return None if __r is None else CommandResponse(__r)

	def restart_safety(self) -> CommandResponse:
		'''Restarts the safety. Used when robot gets a safety fault or violation to restart the safety. After safety has been rebooted the robot will be in Power Off. (From FW 3.7 to 3.12.0 and from 5.1.0)'''
		__r = self._instance.RestartSafety()
		return None if __r is None else CommandResponse(__r)

	def get_safety_status(self) -> CommandResponse1[SafetyStatus]:
		'''Returns the current safety status. (From FW 3.11 to 3.12 and from FW 5.5)'''
		__r = self._instance.GetSafetyStatus()
		return None if __r is None else CommandResponse1[SafetyStatus](None, __r)

	def get_safety_mode(self) -> CommandResponse1[SafetyModes]:
		'''Returns the current safety mode of the robot. An answer that the SDK does not know gives Unknown.

		:returns: The safety mode in Value.
		'''
		__r = self._instance.GetSafetyMode()
		return None if __r is None else CommandResponse1[SafetyModes](None, __r)

	def get_user_role(self) -> CommandResponse1[UserRoles]:
		'''Returns the user role of the robot. See set_user_role().

		:returns: The user role in Value. Succeed is false if the answer is not a known role.
		'''
		__r = self._instance.GetUserRole()
		return None if __r is None else CommandResponse1[UserRoles](None, __r)

	def generate_flight_report(self, reportType: FlightReportTypes) -> CommandResponse1[str]:
		'''Generates a flight report on the robot. This command can take a long time: the SDK waits up to 3 minutes for the answer.

		:param reportType: Type of the report.
		:returns: The identifier of the report in Value.
		'''
		__r = self._instance.GenerateFlightReport(flight_report_types(int(reportType)))
		return None if __r is None else CommandResponse1[str](None, __r)

	def generate_support_file(self, directory: str) -> CommandResponse1[str]:
		'''Generates a support file on the robot. This command can take a long time: the SDK waits up to 10 minutes for the answer.

		:param directory: Existing directory of the robot where the file is saved. It must be inside the programs directory.
		:returns: The name of the support file in Value.
		'''
		__r = self._instance.GenerateSupportFile(directory)
		return None if __r is None else CommandResponse1[str](None, __r)

	def save_log(self) -> CommandResponse:
		'''Saves the log of the robot to its log history file.

		:returns: The answer of the robot.
		'''
		__r = self._instance.SaveLog()
		return None if __r is None else CommandResponse(__r)

	def get_serial_number(self) -> CommandResponse:
		'''Returns serial number of the robot (FW 3.12 and from FW 5.6)'''
		__r = self._instance.GetSerialNumber()
		return None if __r is None else CommandResponse(__r)

	def get_robot_model(self) -> CommandResponse1[RobotModels]:
		'''Returns the robot model (UR3, UR5, UR10, UR16, ...). (FW 3.12 and from FW 5.6)'''
		__r = self._instance.GetRobotModel()
		return None if __r is None else CommandResponse1[RobotModels](None, __r)

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
		'''Event raised when function shutdown() is called.'''
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
