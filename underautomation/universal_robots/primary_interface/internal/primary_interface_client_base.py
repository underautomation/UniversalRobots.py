from __future__ import annotations
import typing
from underautomation.universal_robots.primary_interface.robot_mode_data_package_event_args import RobotModeDataPackageEventArgs
from underautomation.universal_robots.primary_interface.joint_data_package_event_args import JointDataPackageEventArgs
from underautomation.universal_robots.primary_interface.tool_data_package_event_args import ToolDataPackageEventArgs
from underautomation.universal_robots.primary_interface.masterboard_data_package_event_args import MasterboardDataPackageEventArgs
from underautomation.universal_robots.primary_interface.cartesian_info_package_event_args import CartesianInfoPackageEventArgs
from underautomation.universal_robots.primary_interface.kinematics_info_package_event_args import KinematicsInfoPackageEventArgs
from underautomation.universal_robots.primary_interface.configuration_data_package_event_args import ConfigurationDataPackageEventArgs
from underautomation.universal_robots.primary_interface.force_mode_data_package_event_args import ForceModeDataPackageEventArgs
from underautomation.universal_robots.primary_interface.additional_info_package_event_args import AdditionalInfoPackageEventArgs
from underautomation.universal_robots.primary_interface.calibration_data_package_event_args import CalibrationDataPackageEventArgs
from underautomation.universal_robots.primary_interface.safety_data_package_event_args import SafetyDataPackageEventArgs
from underautomation.universal_robots.primary_interface.tool_communication_info_package_event_args import ToolCommunicationInfoPackageEventArgs
from underautomation.universal_robots.primary_interface.tool_mode_info_package_event_args import ToolModeInfoPackageEventArgs
from underautomation.universal_robots.primary_interface.singularity_info_package_event_args import SingularityInfoPackageEventArgs
from underautomation.universal_robots.primary_interface.program_threads_event_args import ProgramThreadsEventArgs
from underautomation.universal_robots.primary_interface.version_event_args import VersionEventArgs
from underautomation.universal_robots.primary_interface.key_message_event_args import KeyMessageEventArgs
from underautomation.universal_robots.primary_interface.popup_message_event_args import PopupMessageEventArgs
from underautomation.universal_robots.primary_interface.text_message_event_args import TextMessageEventArgs
from underautomation.universal_robots.primary_interface.runtime_exception_message_event_args import RuntimeExceptionMessageEventArgs
from underautomation.universal_robots.primary_interface.global_variables import GlobalVariables
from underautomation.universal_robots.primary_interface.internal.primary_interface_script import PrimaryInterfaceScript
from underautomation.universal_robots.primary_interface.internal.primary_interface_commands import PrimaryInterfaceCommands
from underautomation.universal_robots.primary_interface.interfaces import Interfaces
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from underautomation.universal_robots.primary_interface.internal.raw_package_received_event_args import RawPackageReceivedEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface.Internal import PrimaryInterfaceClientBase as primary_interface_client_base
from UnderAutomation.UniversalRobots.PrimaryInterface import Interfaces as interfaces

class PrimaryInterfaceClientBase(URServiceBase):
	'''Base class for the Primary/Secondary Interface client. Manages the TCP connection, decodes incoming binary data packets, and raises events for each decoded sub-package.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = primary_interface_client_base()
		else:
			self._instance = _internal

	def robot_mode_data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.RobotModeDataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def joint_data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.JointDataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def tool_data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ToolDataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def masterboard_data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.MasterboardDataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def cartesian_info_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.CartesianInfoReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def kinematics_info_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.KinematicsInfoReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def configuration_data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ConfigurationDataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def force_mode_data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ForceModeDataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def additional_info_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.AdditionalInfoReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def calibration_data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.CalibrationDataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def safety_data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.SafetyDataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def tool_communication_info_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ToolCommunicationInfoReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def tool_mode_info_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ToolModeInfoReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def singularity_info_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.SingularityInfoReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def package_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.PackageReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def raw_package_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.RawPackageReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def program_threads_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ProgramThreadsReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def version_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.VersionReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def key_message_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.KeyMessageReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def popup_message_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.PopupMessageReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def text_message_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.TextMessageReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def runtime_exception_message_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.RuntimeExceptionMessageReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def disconnect(self) -> None:
		'''Stops data streaming and the possibility to send scripts to the robot.'''
		self._instance.Disconnect()

	@property
	def robot_mode_data(self) -> RobotModeDataPackageEventArgs:
		'''Last Robot mode data received'''
		__r = self._instance.RobotModeData
		return None if __r is None else RobotModeDataPackageEventArgs(__r)

	@property
	def joint_data(self) -> JointDataPackageEventArgs:
		'''Last joint data received'''
		__r = self._instance.JointData
		return None if __r is None else JointDataPackageEventArgs(__r)

	@property
	def tool_data(self) -> ToolDataPackageEventArgs:
		'''Last tool data received'''
		__r = self._instance.ToolData
		return None if __r is None else ToolDataPackageEventArgs(__r)

	@property
	def masterboard_data(self) -> MasterboardDataPackageEventArgs:
		'''Last masterboard data received'''
		__r = self._instance.MasterboardData
		return None if __r is None else MasterboardDataPackageEventArgs(__r)

	@property
	def cartesian_info(self) -> CartesianInfoPackageEventArgs:
		'''Last cartesian information received'''
		__r = self._instance.CartesianInfo
		return None if __r is None else CartesianInfoPackageEventArgs(__r)

	@property
	def kinematics_info(self) -> KinematicsInfoPackageEventArgs:
		'''Last kinematics information received'''
		__r = self._instance.KinematicsInfo
		return None if __r is None else KinematicsInfoPackageEventArgs(__r)

	@property
	def configuration_data(self) -> ConfigurationDataPackageEventArgs:
		'''Last configuration data received'''
		__r = self._instance.ConfigurationData
		return None if __r is None else ConfigurationDataPackageEventArgs(__r)

	@property
	def force_mode_data(self) -> ForceModeDataPackageEventArgs:
		'''Last force mode data received'''
		__r = self._instance.ForceModeData
		return None if __r is None else ForceModeDataPackageEventArgs(__r)

	@property
	def additional_info(self) -> AdditionalInfoPackageEventArgs:
		'''Last additional information received'''
		__r = self._instance.AdditionalInfo
		return None if __r is None else AdditionalInfoPackageEventArgs(__r)

	@property
	def calibration_data(self) -> CalibrationDataPackageEventArgs:
		'''Last calibration data received'''
		__r = self._instance.CalibrationData
		return None if __r is None else CalibrationDataPackageEventArgs(__r)

	@property
	def safety_data(self) -> SafetyDataPackageEventArgs:
		'''Last safety data received'''
		__r = self._instance.SafetyData
		return None if __r is None else SafetyDataPackageEventArgs(__r)

	@property
	def tool_communication_info(self) -> ToolCommunicationInfoPackageEventArgs:
		'''Last tool communication information received'''
		__r = self._instance.ToolCommunicationInfo
		return None if __r is None else ToolCommunicationInfoPackageEventArgs(__r)

	@property
	def tool_mode_info(self) -> ToolModeInfoPackageEventArgs:
		'''Last tool mode information received'''
		__r = self._instance.ToolModeInfo
		return None if __r is None else ToolModeInfoPackageEventArgs(__r)

	@property
	def singularity_info(self) -> SingularityInfoPackageEventArgs:
		'''Last singularity information information received'''
		__r = self._instance.SingularityInfo
		return None if __r is None else SingularityInfoPackageEventArgs(__r)

	@property
	def program_threads(self) -> ProgramThreadsEventArgs:
		'''Last program thread information received'''
		__r = self._instance.ProgramThreads
		return None if __r is None else ProgramThreadsEventArgs(__r)

	@property
	def version(self) -> VersionEventArgs:
		'''Version of the robot and FW'''
		__r = self._instance.Version
		return None if __r is None else VersionEventArgs(__r)

	@property
	def key_message(self) -> KeyMessageEventArgs:
		'''Internal robot events (such as starting or stopping a program)'''
		__r = self._instance.KeyMessage
		return None if __r is None else KeyMessageEventArgs(__r)

	@property
	def popup_message(self) -> PopupMessageEventArgs:
		'''Popup message that appears with the Assignment instruction or the URScript popup() function'''
		__r = self._instance.PopupMessage
		return None if __r is None else PopupMessageEventArgs(__r)

	@property
	def text_message(self) -> TextMessageEventArgs:
		'''Log message sent with URScript instruction textmsg()'''
		__r = self._instance.TextMessage
		return None if __r is None else TextMessageEventArgs(__r)

	@property
	def runtime_exception_message(self) -> RuntimeExceptionMessageEventArgs:
		'''Reports an error in the execution of the program'''
		__r = self._instance.RuntimeExceptionMessage
		return None if __r is None else RuntimeExceptionMessageEventArgs(__r)

	@property
	def global_variables(self) -> GlobalVariables:
		'''List of all variables in current robot program'''
		__r = self._instance.GlobalVariables
		return None if __r is None else GlobalVariables(__r)

	@property
	def script(self) -> PrimaryInterfaceScript:
		'''Contains methods to send custom URScript to the robot'''
		__r = self._instance.Script
		return None if __r is None else PrimaryInterfaceScript(__r)

	@property
	def commands(self) -> PrimaryInterfaceCommands:
		'''Contains methods to send commands to the robot'''
		__r = self._instance.Commands
		return None if __r is None else PrimaryInterfaceCommands(__r)

	@property
	def ip(self) -> str:
		'''IP address of the connected robot'''
		return self._instance.IP

	@property
	def port(self) -> Interfaces:
		'''Interface used for the connected robot'''
		return Interfaces(int(self._instance.Port))

	@property
	def connected(self) -> bool:
		'''Return True if the connection to the robot is active'''
		return self._instance.Connected

	@property
	def local_end_point(self) -> typing.Any:
		'''Indicates the current local endpoint (i.e. IP Address) used to communicate with the robot. You can use this IP in your UR script in the function rpc_factory()'''
		return self._instance.LocalEndPoint

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PrimaryInterfaceClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
