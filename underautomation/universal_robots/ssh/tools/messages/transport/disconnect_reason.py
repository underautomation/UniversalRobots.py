from enum import IntEnum

class DisconnectReason(IntEnum):
	'''Provides list of disconnect reason as specified by the protocol.'''
	None_ = 0 # Disconnect reason is not provided.
	HostNotAllowedToConnect = 1 # SSH_DISCONNECT_HOST_NOT_ALLOWED_TO_CONNECT
	ProtocolError = 2 # SSH_DISCONNECT_PROTOCOL_ERROR
	KeyExchangeFailed = 3 # SSH_DISCONNECT_KEY_EXCHANGE_FAILED
	Reserved = 4 # SSH_DISCONNECT_RESERVED
	MacError = 5 # SSH_DISCONNECT_MAC_ERROR
	CompressionError = 6 # SSH_DISCONNECT_COMPRESSION_ERROR
	ServiceNotAvailable = 7 # SSH_DISCONNECT_SERVICE_NOT_AVAILABLE
	ProtocolVersionNotSupported = 8 # SSH_DISCONNECT_PROTOCOL_VERSION_NOT_SUPPORTED
	HostKeyNotVerifiable = 9 # SSH_DISCONNECT_HOST_KEY_NOT_VERIFIABLE
	ConnectionLost = 10 # SSH_DISCONNECT_CONNECTION_LOST
	ByApplication = 11 # SSH_DISCONNECT_BY_APPLICATION
	TooManyConnections = 12 # SSH_DISCONNECT_TOO_MANY_CONNECTIONS
	AuthenticationCanceledByUser = 13 # SSH_DISCONNECT_AUTH_CANCELLED_BY_USER
	NoMoreAuthenticationMethodsAvailable = 14 # SSH_DISCONNECT_NO_MORE_AUTH_METHODS_AVAILABLE
	IllegalUserName = 15 # SSH_DISCONNECT_ILLEGAL_USER_NAME
