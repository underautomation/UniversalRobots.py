import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Dashboard import UserRoles as user_roles

class UserRoles(int):
	Programmer = user_roles.Programmer
	Operator = user_roles.Operator
	Locked = user_roles.Locked
	restricted = user_roles.restricted
