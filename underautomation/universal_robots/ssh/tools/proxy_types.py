from enum import IntEnum

class ProxyTypes(IntEnum):
	'''Specifies the type of proxy client will use to connect to server.'''
	None_ = 0 # No proxy server.
	Socks4 = 1 # A SOCKS4 proxy server.
	Socks5 = 2 # A SOCKS5 proxy server.
	Http = 3 # A HTTP proxy server.
