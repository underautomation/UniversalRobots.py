from __future__ import annotations
import typing
from UnderAutomation.UniversalRobots.Dashboard.Internal import DashboardClientParametersBase as dashboard_client_parameters_base

class DashboardClientParametersBase:
	'''Abstract base class for Dashboard Server connection parameters, providing default port and timeout values.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dashboard_client_parameters_base()
		else:
			self._instance = _internal

	@property
	def port(self) -> int:
		'''Dashboard client TCP port. Default : 29999'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	@property
	def receive_timeout_ms(self) -> int:
		'''Receive timeout in milliseconds. Default : 2000 ms'''
		return self._instance.ReceiveTimeoutMs

	@receive_timeout_ms.setter
	def receive_timeout_ms(self, value: int):
		self._instance.ReceiveTimeoutMs = value

	@property
	def send_timeout_ms(self) -> int:
		'''Send timeout in milliseconds. Default : 500 ms'''
		return self._instance.SendTimeoutMs

	@send_timeout_ms.setter
	def send_timeout_ms(self, value: int):
		self._instance.SendTimeoutMs = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DashboardClientParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default Dashboard server TCP port
DashboardClientParametersBase.DEFAULT_PORT = dashboard_client_parameters_base.DEFAULT_PORT

# Default receive timeout in milliseconds
DashboardClientParametersBase.DEFAULT_RECEIVE_TIMEOUT_MS = dashboard_client_parameters_base.DEFAULT_RECEIVE_TIMEOUT_MS

# Default send timeout in milliseconds
DashboardClientParametersBase.DEFAULT_SEND_TIMEOUT_MS = dashboard_client_parameters_base.DEFAULT_SEND_TIMEOUT_MS
