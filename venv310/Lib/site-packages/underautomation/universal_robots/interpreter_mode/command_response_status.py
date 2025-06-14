import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.InterpreterMode import CommandResponseStatus as command_response_status

class CommandResponseStatus(int):
	Error = command_response_status.Error
	Ack = command_response_status.Ack
	Discard = command_response_status.Discard
	State = command_response_status.State
