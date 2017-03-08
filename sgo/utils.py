# -*- coding: utf-8 -*-

# flask
from flask import json

# utils
from datetime import datetime
from bson import json_util


def db2dict(src, ban_dct=None):
    if not ban_dct:
        ban_dct = {}
    db_json = json.loads(json_util.dumps(src))
    resp_dict = dict(filter(lambda _: _[0] not in ban_dct, db_json.items()))
    return resp_dict


def db2dict_multi(src, ban_dct=None):
    resp_list = []
    if not ban_dct:
        ban_dct = {}
    if iter(src):
        resp_list = [db2dict(_, ban_dct) for _ in src]
    return resp_list


def check_dict(test, ori):
    """
    check if all keys in test alse in ori recursively
    values of dict can be value, list or dict

    notice: items can't be set type

    :param test:
    :param ori:
    :return:
    """
    flag = True
    for _ in test:
        if _ not in ori:
            return False

        if isinstance(test[_], dict):
            flag = check_dict(test[_], ori[_])
        elif isinstance(test[_], list):
            for item in test[_]:
                # assume ori[_] is list type now
                if isinstance(item, dict):
                    flag = check_dict(item, ori[_][0])
        elif isinstance(test[_], set):
            raise TypeError
    return flag


def timeago(time=False):
    """
    Copy from flask-bones
    Get a datetime object or a int() Epoch timestamp and return a pretty string
    like 'an hour ago', 'Yesterday', '3 months ago', 'just now', etc
    """
    now = datetime.now()
    time = time.replace(tzinfo=None)
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff / 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"
