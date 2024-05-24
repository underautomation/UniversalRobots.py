import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.PrimaryInterface import Interfaces as interfaces

class Interfaces(int):
	PrimaryInterface = interfaces.PrimaryInterface
	SecondaryInterface = interfaces.SecondaryInterface
	PrimaryInterfaceReadOnly = interfaces.PrimaryInterfaceReadOnly
	SecondaryInterfaceReadOnly = interfaces.SecondaryInterfaceReadOnly
