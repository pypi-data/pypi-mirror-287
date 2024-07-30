import marshal
from dataclasses import dataclass, field
from os.path import expanduser
from pathlib import Path


@dataclass
class FileCleanerCache:
    filename: str = expanduser("~/.fc-cache")
    audio_cache: dict = field(default_factory=dict)
    noconvert_list: dict = field(default_factory=list)

    @property
    def cache_value(self):
        return {"audio_cache": self.audio_cache, "noconvert_list": self.noconvert_list}

    @cache_value.setter
    def cache_value(self, val: dict):
        self.audio_cache = val.get("audio_cache", {})
        self.noconvert_list = val.get("noconvert_list", [])

    def save(self):
        with open(self.filename, "wb") as fp:
            marshal.dump(self.cache_value, fp)

    @classmethod
    def from_filename(cls, filename):
        if not Path(filename).is_file():
            cache_value = {}
        else:
            with open(filename, "rb") as fp:
                cache_value = marshal.load(fp)

        inst = cls(filename=filename)
        inst.cache_value = cache_value
        return inst
