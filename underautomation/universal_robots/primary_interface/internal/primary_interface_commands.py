import typing
from underautomation.universal_robots.common.status_code import StatusCode
from underautomation.universal_robots.dashboard.operational_modes import OperationalModes
from underautomation.universal_robots.primary_interface.requested_types import RequestedTypes
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.PrimaryInterface.Internal import PrimaryInterfaceCommands as primary_interface_commands

class PrimaryInterfaceCommands:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = primary_interface_commands()
		else:
			self._instance = _internal
	def test(self) -> None:
		self._instance.Test()
	def power_on(self) -> StatusCode:
		return StatusCode(self._instance.PowerOn())
	def power_off(self) -> StatusCode:
		return StatusCode(self._instance.PowerOff())
	def set_operational_mode(self, mode: OperationalModes) -> StatusCode:
		return StatusCode(self._instance.SetOperationalMode(mode._instance))
	def pause_program(self) -> StatusCode:
		return StatusCode(self._instance.PauseProgram())
	def set_real(self) -> StatusCode:
		return StatusCode(self._instance.SetReal())
	def set_simulated(self) -> StatusCode:
		return StatusCode(self._instance.SetSimulated())
	def stop_program(self) -> StatusCode:
		return StatusCode(self._instance.StopProgram())
	def resume_program(self) -> StatusCode:
		return StatusCode(self._instance.ResumeProgram())
	def step_program(self) -> StatusCode:
		return StatusCode(self._instance.StepProgram())
	def run_program(self) -> StatusCode:
		return StatusCode(self._instance.RunProgram())
	def enable_teach_button(self) -> StatusCode:
		return StatusCode(self._instance.EnableTeachButton())
	def disable_teach_button(self) -> StatusCode:
		return StatusCode(self._instance.DisableTeachButton())
	def enable_freedrive_mode(self) -> StatusCode:
		return StatusCode(self._instance.EnableFreedriveMode())
	def disable_freedrive_mode(self) -> StatusCode:
		return StatusCode(self._instance.DisableFreedriveMode())
	def close_popup(self, id: int) -> StatusCode:
		return StatusCode(self._instance.ClosePopup(id))
	def reply_popup(self, id: int, value: str, type: RequestedTypes) -> StatusCode:
		return StatusCode(self._instance.ReplyPopup(id, value, type._instance))
	def release_brakes(self) -> StatusCode:
		return StatusCode(self._instance.ReleaseBrakes())
	def unlock_protective_stop(self) -> StatusCode:
		return StatusCode(self._instance.UnlockProtectiveStop())
	def increase_speed_limit(self) -> StatusCode:
		return StatusCode(self._instance.IncreaseSpeedLimit())
	def set_speed_limit(self, value: float) -> StatusCode:
		return StatusCode(self._instance.SetSpeedLimit(value))
	def set_speed(self, value: float) -> StatusCode:
		return StatusCode(self._instance.SetSpeed(value))
	def clear_breakpoints(self) -> StatusCode:
		return StatusCode(self._instance.ClearBreakpoints())
	def add_breakpoint(self, line: int, program: str) -> StatusCode:
		return StatusCode(self._instance.AddBreakpoint(line, program))
	def remove_breakpoint(self, line: int, program: str) -> StatusCode:
		return StatusCode(self._instance.RemoveBreakpoint(line, program))
