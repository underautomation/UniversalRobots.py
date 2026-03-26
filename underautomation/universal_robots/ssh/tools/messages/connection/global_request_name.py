from enum import IntEnum

class GlobalRequestName(IntEnum):
	'''Specifies supported request names.'''
	TcpIpForward = 0 # tcpip-forward
	CancelTcpIpForward = 1 # cancel-tcpip-forward
