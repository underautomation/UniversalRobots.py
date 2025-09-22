import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Dashboard.Internal import DashboardClientParametersBase as dashboard_client_parameters_base

class DashboardClientParametersBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dashboard_client_parameters_base()
		else:
			self._instance = _internal
	@property
	def port(self) -> int:
		return self._instance.Port
	@port.setter
	def port(self, value: int):
		self._instance.Port = value
	@property
	def receive_timeout_ms(self) -> int:
		return self._instance.ReceiveTimeoutMs
	@receive_timeout_ms.setter
	def receive_timeout_ms(self, value: int):
		self._instance.ReceiveTimeoutMs = value
	@property
	def send_timeout_ms(self) -> int:
		return self._instance.SendTimeoutMs
	@send_timeout_ms.setter
	def send_timeout_ms(self, value: int):
		self._instance.SendTimeoutMs = value
	@property
	def defaul_t__port(self) -> int:
		return self._instance.DEFAULT_PORT
	@defaul_t__port.setter
	def defaul_t__port(self, value: int):
		self._instance.DEFAULT_PORT = value
	@property
	def defaul_t__receiv_e__timeou_t__ms(self) -> int:
		return self._instance.DEFAULT_RECEIVE_TIMEOUT_MS
	@defaul_t__receiv_e__timeou_t__ms.setter
	def defaul_t__receiv_e__timeou_t__ms(self, value: int):
		self._instance.DEFAULT_RECEIVE_TIMEOUT_MS = value
	@property
	def defaul_t__sen_d__timeou_t__ms(self) -> int:
		return self._instance.DEFAULT_SEND_TIMEOUT_MS
	@defaul_t__sen_d__timeou_t__ms.setter
	def defaul_t__sen_d__timeou_t__ms(self, value: int):
		self._instance.DEFAULT_SEND_TIMEOUT_MS = value
