from __future__ import annotations
import typing
from underautomation.universal_robots.common.robot_dashboard_response import RobotDashboardResponse
from underautomation.universal_robots.common.robot_dashboard_response_1 import RobotDashboardResponse1
from underautomation.universal_robots.dashboard.program_state import ProgramState
from underautomation.universal_robots.common.robot_modes import RobotModes
from underautomation.universal_robots.common.safety_modes import SafetyModes
from underautomation.universal_robots.dashboard.operational_modes import OperationalModes
from underautomation.universal_robots.dashboard.polyscope_version import PolyscopeVersion
from UnderAutomation.UniversalRobots.Common import IRobotDashboard as i_robot_dashboard
from UnderAutomation.UniversalRobots.Common import RobotModes as robot_modes
from UnderAutomation.UniversalRobots.Common import SafetyModes as safety_modes
from UnderAutomation.UniversalRobots.Dashboard import OperationalModes as operational_modes

class IRobotDashboard:
	'''Commands that exist on both the Dashboard Server client (PolyScope 5, CB3 and e-Series) and the REST API client (PolyScope X). Write your code against this interface to control a robot of any of the two families. Both clients implement it explicitly: to call the members, use a variable of type IRobotDashboard. The methods of the clients with the same names keep their own answer types. Every method blocks until the robot answers. A failure is reported in the answer, not by an exception.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_robot_dashboard()
		else:
			self._instance = _internal

	def power_on(self) -> RobotDashboardResponse:
		'''Powers on the robot arm.

		:returns: The answer of the robot.
		'''
		__r = self._instance.PowerOn()
		return None if __r is None else RobotDashboardResponse(__r)

	def power_off(self) -> RobotDashboardResponse:
		'''Powers off the robot arm.

		:returns: The answer of the robot.
		'''
		__r = self._instance.PowerOff()
		return None if __r is None else RobotDashboardResponse(__r)

	def release_brake(self) -> RobotDashboardResponse:
		'''Releases the brakes of the robot.

		:returns: The answer of the robot.
		'''
		__r = self._instance.ReleaseBrake()
		return None if __r is None else RobotDashboardResponse(__r)

	def unlock_protective_stop(self) -> RobotDashboardResponse:
		'''Unlocks a protective stop.

		:returns: The answer of the robot.
		'''
		__r = self._instance.UnlockProtectiveStop()
		return None if __r is None else RobotDashboardResponse(__r)

	def restart_safety(self) -> RobotDashboardResponse:
		'''Restarts the safety system. After the restart the robot is in power off mode.

		:returns: The answer of the robot.
		'''
		__r = self._instance.RestartSafety()
		return None if __r is None else RobotDashboardResponse(__r)

	def load_program(self, programName: str) -> RobotDashboardResponse:
		'''Loads a program of the robot.

		:param programName: Name of the program. The extension is optional.
		:returns: The answer of the robot.
		'''
		__r = self._instance.LoadProgram(programName)
		return None if __r is None else RobotDashboardResponse(__r)

	def get_loaded_program(self) -> RobotDashboardResponse1[str]:
		'''Gets the loaded program.

		:returns: The name or the path of the loaded program in Value.
		'''
		__r = self._instance.GetLoadedProgram()
		return None if __r is None else RobotDashboardResponse1[str](__r)

	def play(self) -> RobotDashboardResponse:
		'''Starts the loaded program.

		:returns: The answer of the robot.
		'''
		__r = self._instance.Play()
		return None if __r is None else RobotDashboardResponse(__r)

	def pause(self) -> RobotDashboardResponse:
		'''Pauses the running program.

		:returns: The answer of the robot.
		'''
		__r = self._instance.Pause()
		return None if __r is None else RobotDashboardResponse(__r)

	def resume(self) -> RobotDashboardResponse:
		'''Resumes the paused program.

		:returns: The answer of the robot.
		'''
		__r = self._instance.Resume()
		return None if __r is None else RobotDashboardResponse(__r)

	def stop(self) -> RobotDashboardResponse:
		'''Stops the running program.

		:returns: The answer of the robot.
		'''
		__r = self._instance.Stop()
		return None if __r is None else RobotDashboardResponse(__r)

	def get_program_state(self) -> RobotDashboardResponse1[ProgramState]:
		'''Gets the state of the program.

		:returns: The state of the program in Value. The name of the program is filled only when the robot gives it.
		'''
		__r = self._instance.GetProgramState()
		return None if __r is None else RobotDashboardResponse1[ProgramState](__r)

	def get_robot_mode(self) -> RobotDashboardResponse1[RobotModes]:
		'''Gets the mode of the robot.

		:returns: The robot mode in Value.
		'''
		__r = self._instance.GetRobotMode()
		return None if __r is None else RobotDashboardResponse1[RobotModes](__r)

	def get_safety_mode(self) -> RobotDashboardResponse1[SafetyModes]:
		'''Gets the safety mode of the robot.

		:returns: The safety mode in Value.
		'''
		__r = self._instance.GetSafetyMode()
		return None if __r is None else RobotDashboardResponse1[SafetyModes](__r)

	def get_operational_mode(self) -> RobotDashboardResponse1[OperationalModes]:
		'''Gets the operational mode of the robot.

		:returns: The operational mode in Value.
		'''
		__r = self._instance.GetOperationalMode()
		return None if __r is None else RobotDashboardResponse1[OperationalModes](__r)

	def is_in_remote_control(self) -> RobotDashboardResponse1[bool]:
		'''Indicates whether the robot is in remote control.

		:returns: True in Value if the robot is in remote control.
		'''
		__r = self._instance.IsInRemoteControl()
		return None if __r is None else RobotDashboardResponse1[bool](__r)

	def show_popup(self, message: str) -> RobotDashboardResponse:
		'''Shows a popup on the screen of the robot.

		:param message: Text of the popup.
		:returns: The answer of the robot.
		'''
		__r = self._instance.ShowPopup(message)
		return None if __r is None else RobotDashboardResponse(__r)

	def close_popup(self) -> RobotDashboardResponse:
		'''Closes the popup of the screen of the robot.

		:returns: The answer of the robot.
		'''
		__r = self._instance.ClosePopup()
		return None if __r is None else RobotDashboardResponse(__r)

	def close_safety_popup(self) -> RobotDashboardResponse:
		'''Closes a safety popup of the screen of the robot.

		:returns: The answer of the robot.
		'''
		__r = self._instance.CloseSafetyPopup()
		return None if __r is None else RobotDashboardResponse(__r)

	def get_polyscope_version(self) -> RobotDashboardResponse1[PolyscopeVersion]:
		'''Gets the version of PolyScope.

		:returns: The version in Value.
		'''
		__r = self._instance.GetPolyscopeVersion()
		return None if __r is None else RobotDashboardResponse1[PolyscopeVersion](__r)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IRobotDashboard):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
