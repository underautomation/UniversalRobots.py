import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.PrimaryInterface import PackageUnit as package_unit

class PackageUnit(int):
	NoUnit = package_unit.NoUnit
	Radian = package_unit.Radian
	RadianPerSecond = package_unit.RadianPerSecond
	RadianPerSecondSquared = package_unit.RadianPerSecondSquared
	Meter = package_unit.Meter
	MeterPerSecond = package_unit.MeterPerSecond
	MeterPersSecondSquared = package_unit.MeterPersSecondSquared
	CelciusDegree = package_unit.CelciusDegree
	Volt = package_unit.Volt
	Amp = package_unit.Amp
