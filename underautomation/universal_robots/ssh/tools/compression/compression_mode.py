from enum import IntEnum

class CompressionMode(IntEnum):
	'''Specifies compression modes'''
	Compress = 0 # Specifies that content should be compressed.
	Decompress = 1 # Specifies that content should be decompressed.
