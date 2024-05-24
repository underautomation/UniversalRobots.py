import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Rtde import RtdeVersions as rtde_versions

class RtdeVersions(int):
	V1 = rtde_versions.V1
	V2 = rtde_versions.V2
