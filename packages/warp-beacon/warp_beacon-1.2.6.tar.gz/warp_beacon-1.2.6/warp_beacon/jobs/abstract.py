from abc import ABC, abstractmethod
from typing import TypedDict
from typing_extensions import Unpack
import uuid

from warp_beacon.jobs import Origin

class JobSettings(TypedDict):
	job_id: uuid.UUID
	message_id: int
	placeholder_message_id: int
	local_media_path: str
	local_compressed_media_path: str
	media_info: dict
	url: str
	uniq_id: str
	tg_file_id: str
	in_process: bool
	media_type: str
	job_failed: bool
	job_failed_msg: str
	job_warning: bool
	job_warning_message: str
	effective_url: str
	save_items: bool
	media_collection: list
	job_origin: Origin
	canonical_name: str

class AbstractJob(ABC):
	job_id: uuid.UUID = None
	message_id: int = 0
	placeholder_message_id: int = 0
	local_media_path: str = ""
	local_compressed_media_path: str = ""
	media_info: dict = {}
	url: str = ""
	uniq_id: str = ""
	tg_file_id: str = ""
	media_type: str = "video"
	in_process: bool = False
	job_warning: bool = False
	job_warning_message: str = ""
	job_failed: bool = False
	job_failed_msg: str = ""
	effective_url: str = ""
	save_items: bool = False
	media_collection: list = []
	job_origin: Origin = Origin.UNKNOWN
	canonical_name: str = ""

	def __init__(self, **kwargs: Unpack[JobSettings]) -> None:
		if kwargs:
			self.__dict__.update(kwargs)
		self.job_id = uuid.uuid4()

	def __del__(self) -> None:
		pass

	def __str__(self) -> str:
		return str(self.to_dict())

	def __repr__(self) -> str:
		return str(self.to_dict())

	def is_empty(self) -> bool:
		if self.media_type == "collection":
			if not self.media_collection:
				return True
		elif not self.local_media_path:
			return True
		return False

	def to_dict(self) -> dict:
		d = {}
		for key in dir(self.__class__):
			if not key.startswith('_'):
				value = getattr(self, key)
				if not callable(value):
					d[key] = value
					
		return d