"""
models for sgo
"""
from sgo.utils import check_dict


class ModelMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'doc' in kwargs:
            cls.doc = kwargs['doc']
        elif isinstance(cls.MOD, dict):
            cls.doc = cls.MOD
        else:
            raise AttributeError


class BaseModel(metaclass=ModelMeta):
    """

    Base Class of all Model of sgo
    Use pymongo as backend

    Assume: item is not set type

    """
    MOD = {}
    doc = {}

    def check(self):
        """
        check all key in self.doc also in self.MOD recursively
        :return: True or False
        """
        check_dict(self.doc, self.MOD)

    def req_args(self):
        return NotImplemented
