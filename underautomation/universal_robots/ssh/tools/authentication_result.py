from enum import IntEnum

class AuthenticationResult(IntEnum):
	'''Represents possible authentication methods results'''
	Success = 0 # Authentication was successful.
	PartialSuccess = 1 # Authentication completed with partial success.
	Failure = 2 # Authentication failed.
