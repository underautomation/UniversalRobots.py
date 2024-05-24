import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Common import DigitalOutputConfigurations as digital_output_configurations

class DigitalOutputConfigurations(int):
	SinkingNPN = digital_output_configurations.SinkingNPN
	SourcingPNP = digital_output_configurations.SourcingPNP
	PushPull = digital_output_configurations.PushPull
