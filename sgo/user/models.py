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
    _ban_list = ['pw', 'balance', 'credit', 'tasks']

    MOD = {
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
    }

    def req_args(self):
        """
        :return: assume all items in args are str
        which would be used in views
        """
        args = []
        for _ in self.MOD:
            if _ not in self._ban_list:
                args.append(_)
        return args


class Followers(BaseModel):
    MOD = {
        "idol_id": "",
        "fans_id": ""
    }
