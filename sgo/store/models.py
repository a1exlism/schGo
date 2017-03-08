# -*- coding: utf-8 -*-

from sgo.models import BaseModel


class Task(BaseModel):
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
        "form": {
            "detail": "",
            "landmark": "",
            "campus": "",
            "school": ""
        },
        "to": {
            "detail": "",
            "landmark": "",
            "campus": "",
            "school": ""
        }
    }


class Product(BaseModel):
    _MOD = {
        "publisher": {
            "id": "",
            "name": "",
            "avatar_url": ""
        },
        "pub_time": "",
        "desc": "",
        "params": {
            "pic_url": "",
            "video_url": "",
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
