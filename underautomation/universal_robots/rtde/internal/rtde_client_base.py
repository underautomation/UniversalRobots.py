import typing
from __future__ import annotation
from underautomation.universal_robots.rtde.rtde_text_message_event_args import RtdeTextMessageEventArgs
from underautomation.universal_robots.rtde.rtde_states import RTDEStates
from underautomation.universal_robots.rtde.rtde_versions import RtdeVersions
from underautomation.universal_robots.rtde.rtde_output_setup_item import RtdeOutputSetupItem
from underautomation.universal_robots.rtde.rtde_input_setup_item import RtdeInputSetupItem
from underautomation.universal_robots.rtde.rtde_output_values import RtdeOutputValues
from underautomation.universal_robots.rtde.rtde_input_values import RtdeInputValues
from underautomation.universal_robots.internal.ur_service_base import URServiceBase
from underautomation.universal_robots.rtde.rtde_protocol_version_event_args import RtdeProtocolVersionEventArgs
from underautomation.universal_robots.rtde.rtde_data_package_event_args import RtdeDataPackageEventArgs
from underautomation.universal_robots.rtde.rtde_control_package_setup_outputs_event_args import RtdeControlPackageSetupOutputsEventArgs
from underautomation.universal_robots.rtde.rtde_control_package_setup_inputs_event_args import RtdeControlPackageSetupInputsEventArgs
from underautomation.universal_robots.rtde.rtde_basic_request_event_args import RtdeBasicRequestEventArgs
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.Rtde.Internal import RtdeClientBase as rtde_client_base
from UnderAutomation.UniversalRobots.Rtde import RTDEStates as rtde_states
from UnderAutomation.UniversalRobots.Rtde import RtdeVersions as rtde_versions

class RtdeClientBase(URServiceBase):
	'''Base class common to all RTDE clients'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_client_base()
		else:
			self._instance = _internal

	def protocol_version_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ProtocolVersionReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def text_message_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.TextMessageReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def output_data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.OutputDataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def setup_outputs_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.SetupOutputsReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def setup_inputs_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.SetupInputsReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def start_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.StartReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def pause_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.PauseReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def package_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.PackageReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def pause(self) -> None:
		'''Pause data streaming without disconnecting client'''
		self._instance.Pause()

	def resume(self) -> None:
		'''Restart data streaming after a Pause'''
		self._instance.Resume()

	def write_inputs(self, inputValues: RtdeInputValues) -> None:
		'''Write data to controller. Data must be those selected in connect parameters'''
		self._instance.WriteInputs(inputValues._instance if inputValues else None)

	def disconnect(self) -> None:
		'''Close the RTDE connection to the robot'''
		self._instance.Disconnect()

	@property
	def last_text_message(self) -> RtdeTextMessageEventArgs:
		'''Last text received from the robot'''
		return RtdeTextMessageEventArgs(self._instance.LastTextMessage)

	@property
	def state(self) -> RTDEStates:
		'''Current RTDE state'''
		return RTDEStates(int(self._instance.State))

	@property
	def connected(self) -> bool:
		'''Gets a value indicating if RTDE client is connected to the robot'''
		return self._instance.Connected

	@property
	def ip(self) -> str:
		'''IP address of the robot'''
		return self._instance.IP

	@property
	def applied_frequency(self) -> float:
		'''Output data frequency requested to the robot, only for RTDE version 2'''
		return self._instance.AppliedFrequency

	@property
	def version(self) -> RtdeVersions:
		'''Current protocol version used to stream data'''
		return RtdeVersions(int(self._instance.Version))

	@property
	def output_setup(self) -> typing.List[RtdeOutputSetupItem]:
		'''List of all data sent from the robot to the PC (robot point of view)'''
		return [RtdeOutputSetupItem(None, None, x) for x in self._instance.OutputSetup]

	@property
	def input_setup(self) -> typing.List[RtdeInputSetupItem]:
		'''List of all data the PC can write to the robot (robot point of view)'''
		return [RtdeInputSetupItem(None, None, x) for x in self._instance.InputSetup]

	@property
	def output_recipe_id(self) -> int:
		'''Recipe Identifier of output received data'''
		return self._instance.OutputRecipeId

	@property
	def input_recipe_id(self) -> int:
		'''Recipe Identifier of input sent data'''
		return self._instance.InputRecipeId

	@property
	def input_recipe_is_valid(self) -> bool:
		'''Indicates that the recipe is valid, i.e. that all the registers have been found and are not already reserved for writing by another RTDE client. Check event SetupInputsReceived to see which registers are NOT_FOUND or IN_USE'''
		return self._instance.InputRecipeIsValid

	@property
	def measured_frequency(self) -> float:
		'''Measured output data packet frequency. "Timestamp" output data shoud be part of output setup to measure frequency.'''
		return self._instance.MeasuredFrequency

	@property
	def output_data_values(self) -> RtdeOutputValues:
		'''Last data received from the robot'''
		return RtdeOutputValues(self._instance.OutputDataValues)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
