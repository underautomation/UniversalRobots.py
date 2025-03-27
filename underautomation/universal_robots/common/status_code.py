import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import StatusCode as status_code

class StatusCode(int):
	OK = status_code.OK
	ReadThreadAborted = status_code.ReadThreadAborted
	DecodageError = status_code.DecodageError
	SendCommandInternalError = status_code.SendCommandInternalError
	SentCommandIsEmpty = status_code.SentCommandIsEmpty
	StreamingInterfaceNotConnected = status_code.StreamingInterfaceNotConnected
	XmlRpcInternalError = status_code.XmlRpcInternalError
	GlobalVariablesError = status_code.GlobalVariablesError
	SocketInternalError = status_code.SocketInternalError
	RTDEThreadAborted = status_code.RTDEThreadAborted
	WriteInputsRtdeError = status_code.WriteInputsRtdeError
	RTDEOverrun = status_code.RTDEOverrun
