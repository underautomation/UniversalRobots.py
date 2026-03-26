import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Ssh.Tools import ExpectAction as expect_action

class ExpectAction:
	'''Specifies behavior for expected expression'''
	def __init__(self, expect: typing.Any, action: typing.Any, _internal = 0):
		if(_internal == 0):
			self._instance = expect_action(expect, action)
		else:
			self._instance = _internal

	@property
	def expect(self) -> typing.Any:
		'''Gets the expected regular expression.'''
		return self._instance.Expect

	@property
	def action(self) -> typing.Any:
		'''Gets the action to perform when expected expression is found.'''
		return self._instance.Action

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ExpectAction):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
