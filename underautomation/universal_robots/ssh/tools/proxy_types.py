import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Ssh.Tools import ProxyTypes as proxy_types

class ProxyTypes(int):
	Socks4 = proxy_types.Socks4
	Socks5 = proxy_types.Socks5
	Http = proxy_types.Http
