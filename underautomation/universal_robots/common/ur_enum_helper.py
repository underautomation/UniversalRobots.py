from __future__ import annotations
import typing
from underautomation.universal_robots.common.robot_models import RobotModels
from underautomation.universal_robots.common.robot_modes import RobotModes
from underautomation.universal_robots.common.safety_modes import SafetyModes
from underautomation.universal_robots.common.robot_series import RobotSeries
from underautomation.universal_robots.common.control_box_type import ControlBoxType
from underautomation.universal_robots.common.tool_flange_type import ToolFlangeType
from UnderAutomation.UniversalRobots.Common import UrEnumHelper as ur_enum_helper
from UnderAutomation.UniversalRobots.Common import RobotModels as robot_models
from UnderAutomation.UniversalRobots.Common import RobotModes as robot_modes
from UnderAutomation.UniversalRobots.Common import SafetyModes as safety_modes
from UnderAutomation.UniversalRobots.Common import RobotSeries as robot_series
from UnderAutomation.UniversalRobots.Common import ControlBoxType as control_box_type
from UnderAutomation.UniversalRobots.Common import ToolFlangeType as tool_flange_type

class UrEnumHelper:
	'''Conversions from the raw numbers sent by a robot to the enums of the SDK. An unknown number never throws: the result is the Unknown value of the enum.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ur_enum_helper()
		else:
			self._instance = _internal

	@staticmethod
	def robot_model_from_value(value: int) -> RobotModels:
		'''Converts a raw robot model number to RobotModels.

		:param value: Raw robot model number.
		:returns: The model, or Unknown if the number is not known.
		'''
		return RobotModels(int(ur_enum_helper.RobotModelFromValue(value)))

	@staticmethod
	def robot_mode_from_value(value: int) -> RobotModes:
		'''Converts a raw robot mode number to RobotModes.

		:param value: Raw robot mode number.
		:returns: The mode, or Unknown if the number is not known.
		'''
		return RobotModes(int(ur_enum_helper.RobotModeFromValue(value)))

	@staticmethod
	def safety_mode_from_value(value: int) -> SafetyModes:
		'''Converts a raw safety mode number to SafetyModes.

		:param value: Raw safety mode number.
		:returns: The safety mode, or Unknown if the number is not known.
		'''
		return SafetyModes(int(ur_enum_helper.SafetyModeFromValue(value)))

	@staticmethod
	def robot_series_from_value(value: int) -> RobotSeries:
		'''Converts a raw robot series number to RobotSeries.

		:param value: Raw series number: 1 for CB3, 2 for e-Series, 3 for UR Series, 4 for G Series.
		:returns: The series, or Unknown if the number is not known.
		'''
		return RobotSeries(int(ur_enum_helper.RobotSeriesFromValue(value)))

	@staticmethod
	def robot_series_from_model(model: RobotModels, softwareMajor: int, softwareMinor: int) -> RobotSeries:
		'''Finds the series of a robot from its model and its software version.

		:param model: Robot model.
		:param softwareMajor: Major version of the software (3 or 5 for PolyScope, 10 for PolyScope X).
		:param softwareMinor: Minor version of the software.
		:returns: The series, or Unknown if the model and the version do not match a series.
		'''
		return RobotSeries(int(ur_enum_helper.RobotSeriesFromModel(robot_models(int(model)), softwareMajor, softwareMinor)))

	@staticmethod
	def control_box_type_from_value(value: int) -> ControlBoxType:
		'''Converts a raw control box number to ControlBoxType. Both numberings sent by the robots are accepted: 1 and 5 mean CB5, 2 and 7 mean CB7.

		:param value: Raw control box number.
		:returns: The control box type, or Unknown if the number is not known.
		'''
		return ControlBoxType(int(ur_enum_helper.ControlBoxTypeFromValue(value)))

	@staticmethod
	def tool_flange_type_from_value(value: int) -> ToolFlangeType:
		'''Converts a raw tool flange number to ToolFlangeType.

		:param value: Raw tool flange number: 1 for V1, 2 for V2.
		:returns: The tool flange type, or Unknown if the number is not known.
		'''
		return ToolFlangeType(int(ur_enum_helper.ToolFlangeTypeFromValue(value)))

	@staticmethod
	def is_protective_stopped(mode: SafetyModes) -> bool:
		'''Tells if the safety mode is a protective, safeguard or enabling device stop. Emergency stops, faults and violations are not included.

		:param mode: Safety mode.
		:returns: True if the robot is stopped by a protective, safeguard or enabling device stop.
		'''
		return ur_enum_helper.IsProtectiveStopped(safety_modes(int(mode)))

	@staticmethod
	def safety_mode_allows_execution(mode: SafetyModes) -> bool:
		'''Tells if the safety mode lets the robot move and run a program: Normal or Reduced.

		:param mode: Safety mode.
		:returns: True for Normal and Reduced.
		'''
		return ur_enum_helper.SafetyModeAllowsExecution(safety_modes(int(mode)))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UrEnumHelper):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
