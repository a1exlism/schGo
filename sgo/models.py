"""
models for sgo
"""
from sgo.utils import check_dict


class ModelMeta(type):
    pass
    # def __init__(cls, *args, **kwargs):
    #     if 'doc' in kwargs:
    #         cls.doc = kwargs['doc']
    #     elif isinstance(cls._MOD, dict):
    #         cls.doc = cls._MOD
    #     else:
    #         cls.doc = None
    #     super().__init__(*args, **kwargs)


class BaseModel(metaclass=ModelMeta):
    """

    Base Class of all Model of sgo
    Use pymongo as backend

    Assume: item is not set type

    """
    _MOD = {}

    def __init__(self, *args, **kwargs):
        if 'doc' in kwargs:
            self.doc = kwargs['doc']
        elif isinstance(self._MOD, dict):
            self.doc = self._MOD.copy()
        else:
            self.doc = {}

    def check(self):
        """
        check all key in self.doc also in self.MOD recursively
        :return: True or False
        """
        if self.doc:
            check_dict(self.doc, self._MOD)
        else:
            raise AttributeError

    def req_args(self):
        return NotImplemented
