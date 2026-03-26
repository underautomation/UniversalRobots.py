import typing
from __future__ import annotation
from underautomation.universal_robots.common.package_event_args import PackageEventArgs
from UnderAutomation.UniversalRobots.PrimaryInterface import RuntimeExceptionMessageEventArgs as runtime_exception_message_event_args

class RuntimeExceptionMessageEventArgs(PackageEventArgs):
	'''Reports an error in the execution of the program'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = runtime_exception_message_event_args()
		else:
			self._instance = _internal

	@property
	def script_line_number(self) -> int:
		'''Execution error line number'''
		return self._instance.ScriptLineNumber

	@script_line_number.setter
	def script_line_number(self, value: int):
		self._instance.ScriptLineNumber = value

	@property
	def script_column_number(self) -> int:
		'''Execution error column number'''
		return self._instance.ScriptColumnNumber

	@script_column_number.setter
	def script_column_number(self, value: int):
		self._instance.ScriptColumnNumber = value

	@property
	def runtime_exception_text_message(self) -> str:
		'''Information about exception'''
		return self._instance.RuntimeExceptionTextMessage

	@runtime_exception_text_message.setter
	def runtime_exception_text_message(self, value: str):
		self._instance.RuntimeExceptionTextMessage = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RuntimeExceptionMessageEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
