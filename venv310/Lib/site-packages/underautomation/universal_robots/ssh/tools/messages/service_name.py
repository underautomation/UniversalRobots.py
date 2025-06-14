import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Ssh.Tools.Messages import ServiceName as service_name

class ServiceName(int):
	UserAuthentication = service_name.UserAuthentication
	Connection = service_name.Connection
