# -*- coding: utf-8 -*-

from sgo.extensions import pm

# json
from bson import json_util
from sgo.models import BaseModel
from sgo.utils import check_dict

FOLLOWING_MAX = 1000
FOLLOWERS_MAX = 1000


class User(BaseModel):
    """
    > If the document dose not have an _id field
    > one will be added automatically

    """
    _ban_list = {'pw', 'balance', 'credit', 'tasks'}

    _MOD = {
        "id": "",  # unique and pretty
        "pw": "",
        "name": "",
        "email": "",
        "phone": "",
        "bio": "",
        "school": "",
        "avatar_url": "",
        "qq": "",
        "weibo": "",
        "wechat": "",
        "balance": 0,
        "credit": 0,
        "tasks": [],
        "products": []
    }

    def req_args(self):
        """
        :return: assume all items in args are str
        which would be used in views
        """
        args = []
        for _ in self._MOD:
            if _ not in self._ban_list:
                args.append(_)
        return args

    def to_doc(self, user):
        if self.doc:
            raise ValueError


class Followers(BaseModel):
    _MOD = {
        "idol_id": "",
        "fans_id": ""
    }
