# -*- coding: utf-8 -*-

from sgo.models import BaseModel


class Task(BaseModel):
    _ban_list = {}
    _MOD = {
        "place": "",
        "publisher": {
            "id": "",
            "name": "",
            "avatar_url": ""
        },
        "receiver_id": "",
        "desc": "",
        "reward": 0,
        "pub_time": "",
        "from_": {
            "detail": "",
            "landmark": "",
            "campus": "",
            "school": ""
        },
        "to_": {
            "detail": "",
            "landmark": "",
            "campus": "",
            "school": ""
        },
        "tags": [],
        "comments": [
            {
                "floor": 0,
                "author": "",
                "author_id": "",
                "datetime": "",
                "content": "",
                "likes": 0
            }
        ]
    }


class Product(BaseModel):
    _ban_list = {}
    _MOD = {
        "publisher": {
            "id": "",
            "name": "",
            "avatar_url": ""
        },
        "pub_time": "",
        "price": 0,
        "desc": "",
        "pic_url": [],
        "video_url": [],
        "info": {
            "views": 0,
            "likes": 0
        },
        "tags": [],
        "comments": [
            {
                "floor": 0,
                "author": "",
                "author_id": "",
                "datetime": "",
                "content": "",
                "likes": 0
            }
        ]
    }


# 优惠
class Preferential(object):
    pass
