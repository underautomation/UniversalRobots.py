import typing
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
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rtde.Internal import RtdeClientBase as rtde_client_base

class RtdeClientBase(URServiceBase):
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
		self._instance.Pause()
	def resume(self) -> None:
		self._instance.Resume()
	def write_inputs(self, inputValues: RtdeInputValues) -> None:
		self._instance.WriteInputs(inputValues._instance)
	def disconnect(self) -> None:
		self._instance.Disconnect()
	@property
	def last_text_message(self) -> RtdeTextMessageEventArgs:
		return RtdeTextMessageEventArgs(self._instance.LastTextMessage)
	@property
	def state(self) -> RTDEStates:
		return RTDEStates(self._instance.State)
	@property
	def connected(self) -> bool:
		return self._instance.Connected
	@property
	def ip(self) -> str:
		return self._instance.IP
	@property
	def applied_frequency(self) -> float:
		return self._instance.AppliedFrequency
	@property
	def version(self) -> RtdeVersions:
		return RtdeVersions(self._instance.Version)
	@property
	def output_setup(self) -> typing.List[RtdeOutputSetupItem]:
		return [RtdeOutputSetupItem(x) for x in self._instance.OutputSetup]
	@property
	def input_setup(self) -> typing.List[RtdeInputSetupItem]:
		return [RtdeInputSetupItem(x) for x in self._instance.InputSetup]
	@property
	def output_recipe_id(self) -> int:
		return self._instance.OutputRecipeId
	@property
	def input_recipe_id(self) -> int:
		return self._instance.InputRecipeId
	@property
	def input_recipe_is_valid(self) -> bool:
		return self._instance.InputRecipeIsValid
	@property
	def measured_frequency(self) -> float:
		return self._instance.MeasuredFrequency
	@property
	def output_data_values(self) -> RtdeOutputValues:
		return RtdeOutputValues(self._instance.OutputDataValues)
