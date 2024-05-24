import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Ssh.Tools.Messages.Connection import GlobalRequestName as global_request_name

class GlobalRequestName(int):
	TcpIpForward = global_request_name.TcpIpForward
	CancelTcpIpForward = global_request_name.CancelTcpIpForward
