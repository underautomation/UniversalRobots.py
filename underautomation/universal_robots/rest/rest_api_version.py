import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rest import RestApiVersion as rest_api_version

class RestApiVersion(int):
	V1 = rest_api_version.V1
	Latest = rest_api_version.Latest
