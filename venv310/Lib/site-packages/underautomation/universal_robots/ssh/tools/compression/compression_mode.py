import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Ssh.Tools.Compression import CompressionMode as compression_mode

class CompressionMode(int):
	Compress = compression_mode.Compress
	Decompress = compression_mode.Decompress
