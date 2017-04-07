"""
models for sgo
"""
# sgo
from ..utils import check_dict
from ..config import BaseConfig
from ..structures import LookupDict

from enum import Enum


class DataType(Enum):
    Integer = 'int'
    String = 'str'
    List = 'list'


class ModelMeta(type):
    pass


class BaseModel(metaclass=ModelMeta):
    """

    Base Class of all Model of sgo
    Use pymongo as backend

    Assume: item is not set type

    """
    _MOD = dict()

    _register = {
        "key_name: [type, validate_func]"
    }

    def __init__(self, doc=None, *args, **kwargs):
        if doc:
            self.doc = doc
        else:
            if isinstance(self._MOD, dict):
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


# TODO: finish this test
def check_model(model):
    """Check is there any attribute collide in model"""
    pass
