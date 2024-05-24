import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Ssh.Tools.Messages.Transport import DisconnectReason as disconnect_reason

class DisconnectReason(int):
	HostNotAllowedToConnect = disconnect_reason.HostNotAllowedToConnect
	ProtocolError = disconnect_reason.ProtocolError
	KeyExchangeFailed = disconnect_reason.KeyExchangeFailed
	Reserved = disconnect_reason.Reserved
	MacError = disconnect_reason.MacError
	CompressionError = disconnect_reason.CompressionError
	ServiceNotAvailable = disconnect_reason.ServiceNotAvailable
	ProtocolVersionNotSupported = disconnect_reason.ProtocolVersionNotSupported
	HostKeyNotVerifiable = disconnect_reason.HostKeyNotVerifiable
	ConnectionLost = disconnect_reason.ConnectionLost
	ByApplication = disconnect_reason.ByApplication
	TooManyConnections = disconnect_reason.TooManyConnections
	AuthenticationCanceledByUser = disconnect_reason.AuthenticationCanceledByUser
	NoMoreAuthenticationMethodsAvailable = disconnect_reason.NoMoreAuthenticationMethodsAvailable
	IllegalUserName = disconnect_reason.IllegalUserName
