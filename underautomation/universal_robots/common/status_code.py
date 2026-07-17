from enum import IntEnum

class StatusCode(IntEnum):
	'''Status code that describes an internal error or an internal action'''
	OK = 0 # The action succeeded
	ReadThreadAborted = 1 # The read thread has stopped due to an internal exception. No more data event will be raised.
	DecodageError = 2 # The data received are inconsistent and it not possible to decode it.
	SendCommandInternalError = 3 # Unable to send URScript because of an internal error.
	SentCommandIsEmpty = 4 # Unable to send URScript because the script sent is empty.
	StreamingInterfaceNotConnected = 5 # Streaming interface is not connected
	XmlRpcInternalError = 6 # An error occured in the XML-RPC server
	GlobalVariablesError = 7 # An error occured while decoding global variables
	SocketInternalError = 8 # An error occured while handling socket packet
	RTDEThreadAborted = 9 # The RTDE read thread has stopped due to an internal exception. No more data event will be raised.
	WriteInputsRtdeError = 10 # Error occured while writing RTDE input data
	RTDEOverrun = 11 # RTDE Event handler takes longer to execute than the time between each RTDE packets
