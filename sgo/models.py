"""
models for sgo
"""
from sgo.utils import check_dict
from sgo.config import BaseConfig


class ModelMeta(type):
    pass


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


class Admin:
    def __init__(self):
        self.id = 'jesus'
        self.password = BaseConfig.ADMIN_PW

    # flask_login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def validate_pw(self, str):
        if self.password != str:
            return False
        return True

    # Required for flask-login interface
    def __str__(self):
        return self.id
