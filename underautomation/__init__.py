import clr
import os

_dll_path = os.path.realpath(os.path.join(os.path.dirname(__file__), 'universal_robots', 'lib', 'UnderAutomation.UniversalRobots.dll'))
clr.AddReference(_dll_path)

__author__ = 'UnderAutomation'
