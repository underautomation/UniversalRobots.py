from enum import IntEnum

class ServiceName(IntEnum):
	'''Specifies list of supported services'''
	UserAuthentication = 0 # ssh-userauth
	Connection = 1 # ssh-connection
