import typing
from __future__ import annotation
from UnderAutomation.UniversalRobots.Ssh.Tools.Sftp import SftpFileSytemInformation as sftp_file_sytem_information

class SftpFileSytemInformation:
	'''Contains File system information exposed by statvfs@openssh.com request.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sftp_file_sytem_information()
		else:
			self._instance = _internal

	@property
	def file_system_block_size(self) -> int:
		'''Gets the file system block size.'''
		return self._instance.FileSystemBlockSize

	@property
	def block_size(self) -> int:
		'''Gets the fundamental file system size of the block.'''
		return self._instance.BlockSize

	@property
	def total_blocks(self) -> int:
		'''Gets the total blocks.'''
		return self._instance.TotalBlocks

	@property
	def free_blocks(self) -> int:
		'''Gets the free blocks.'''
		return self._instance.FreeBlocks

	@property
	def available_blocks(self) -> int:
		'''Gets the available blocks.'''
		return self._instance.AvailableBlocks

	@property
	def total_nodes(self) -> int:
		'''Gets the total nodes.'''
		return self._instance.TotalNodes

	@property
	def free_nodes(self) -> int:
		'''Gets the free nodes.'''
		return self._instance.FreeNodes

	@property
	def available_nodes(self) -> int:
		'''Gets the available nodes.'''
		return self._instance.AvailableNodes

	@property
	def sid(self) -> int:
		'''Gets the sid.'''
		return self._instance.Sid

	@property
	def is_read_only(self) -> bool:
		'''Gets a value indicating whether this instance is read only.'''
		return self._instance.IsReadOnly

	@property
	def supports_set_uid(self) -> bool:
		'''Gets a value indicating whether [supports set uid].'''
		return self._instance.SupportsSetUid

	@property
	def max_name_lenght(self) -> int:
		'''Gets the max name lenght.'''
		return self._instance.MaxNameLenght

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SftpFileSytemInformation):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
