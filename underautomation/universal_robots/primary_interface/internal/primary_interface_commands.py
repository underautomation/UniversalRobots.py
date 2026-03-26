import typing
from __future__ import annotation
from underautomation.universal_robots.common.status_code import StatusCode
from underautomation.universal_robots.dashboard.operational_modes import OperationalModes
from underautomation.universal_robots.primary_interface.requested_types import RequestedTypes
from UnderAutomation.UniversalRobots.PrimaryInterface.Internal import PrimaryInterfaceCommands as primary_interface_commands
from UnderAutomation.UniversalRobots.Common import StatusCode as status_code
from UnderAutomation.UniversalRobots.Dashboard import OperationalModes as operational_modes
from UnderAutomation.UniversalRobots.PrimaryInterface import RequestedTypes as requested_types

class PrimaryInterfaceCommands:
	'''Handles Primary interface commands'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = primary_interface_commands()
		else:
			self._instance = _internal

	def test(self) -> None:
		'''Sends a test HMC expression parse command to the robot (for internal debugging).'''
		self._instance.Test()

	def power_on(self) -> StatusCode:
		'''Power on the robot'''
		return StatusCode(int(self._instance.PowerOn()))

	def power_off(self) -> StatusCode:
		'''Power off the robot'''
		return StatusCode(int(self._instance.PowerOff()))

	def set_operational_mode(self, mode: OperationalModes) -> StatusCode:
		'''Set robot operational mode'''
		return StatusCode(int(self._instance.SetOperationalMode(operational_modes(int(mode)))))

	def pause_program(self) -> StatusCode:
		'''Pause running program'''
		return StatusCode(int(self._instance.PauseProgram()))

	def set_real(self) -> StatusCode:
		'''Set robot to real robot (disable simulation)'''
		return StatusCode(int(self._instance.SetReal()))

	def set_simulated(self) -> StatusCode:
		'''Simulate robot'''
		return StatusCode(int(self._instance.SetSimulated()))

	def stop_program(self) -> StatusCode:
		'''Stop running program'''
		return StatusCode(int(self._instance.StopProgram()))

	def resume_program(self) -> StatusCode:
		'''Resume paused program'''
		return StatusCode(int(self._instance.ResumeProgram()))

	def step_program(self) -> StatusCode:
		'''Step program execution. Should be followed by ResumeProgram() to move to next instruction'''
		return StatusCode(int(self._instance.StepProgram()))

	def run_program(self) -> StatusCode:
		'''Run program from start'''
		return StatusCode(int(self._instance.RunProgram()))

	def enable_teach_button(self) -> StatusCode:
		'''Enable teach button'''
		return StatusCode(int(self._instance.EnableTeachButton()))

	def disable_teach_button(self) -> StatusCode:
		'''Disable teach button'''
		return StatusCode(int(self._instance.DisableTeachButton()))

	def enable_freedrive_mode(self) -> StatusCode:
		'''Enable freedrive mode'''
		return StatusCode(int(self._instance.EnableFreedriveMode()))

	def disable_freedrive_mode(self) -> StatusCode:
		'''Disable freedrive mode'''
		return StatusCode(int(self._instance.DisableFreedriveMode()))

	def close_popup(self, id: int) -> StatusCode:
		'''Close popup'''
		return StatusCode(int(self._instance.ClosePopup(id)))

	def reply_popup(self, id: int, value: str, type: RequestedTypes) -> StatusCode:
		'''Reply popup'''
		return StatusCode(int(self._instance.ReplyPopup(id, value, requested_types(int(type)))))

	def release_brakes(self) -> StatusCode:
		'''Release brakes'''
		return StatusCode(int(self._instance.ReleaseBrakes()))

	def unlock_protective_stop(self) -> StatusCode:
		'''Unlock protective stop'''
		return StatusCode(int(self._instance.UnlockProtectiveStop()))

	def increase_speed_limit(self) -> StatusCode:
		'''Increase speed limit'''
		return StatusCode(int(self._instance.IncreaseSpeedLimit()))

	def set_speed_limit(self, value: float) -> StatusCode:
		'''Set speed limit'''
		return StatusCode(int(self._instance.SetSpeedLimit(value)))

	def set_speed(self, value: float) -> StatusCode:
		'''Set speed'''
		return StatusCode(int(self._instance.SetSpeed(value)))

	def clear_breakpoints(self) -> StatusCode:
		'''Clear all breakpoints'''
		return StatusCode(int(self._instance.ClearBreakpoints()))

	def add_breakpoint(self, line: int, program: str) -> StatusCode:
		'''Add a new breakpoint'''
		return StatusCode(int(self._instance.AddBreakpoint(line, program)))

	def remove_breakpoint(self, line: int, program: str) -> StatusCode:
		'''Remove an existing breakpoint'''
		return StatusCode(int(self._instance.RemoveBreakpoint(line, program)))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PrimaryInterfaceCommands):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
