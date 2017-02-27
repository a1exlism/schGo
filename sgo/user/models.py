# -*- coding: utf-8 -*-

from sgo.extensions import pm

# json
from bson import json_util
from sgo.models import BaseModel

FOLLOWING_MAX = 1000
FOLLOWERS_MAX = 1000


class User(BaseModel):
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


class Followers(BaseModel):
    MOD = {
        "idol_id": "",
        "fans_id": ""
    }
