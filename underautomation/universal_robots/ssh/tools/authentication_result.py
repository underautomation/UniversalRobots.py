import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Ssh.Tools import AuthenticationResult as authentication_result

class AuthenticationResult(int):
	Success = authentication_result.Success
	PartialSuccess = authentication_result.PartialSuccess
	Failure = authentication_result.Failure
