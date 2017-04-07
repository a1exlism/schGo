# -*- coding: utf-8 -*-

# flask
from flask import json

# utils
from bson import json_util


def db2dict(src, ban_dct=None):
    """

    :param src: database result object
    :param ban_dct: forbidden keys
    :return:
    """
    if not ban_dct:
        ban_dct = {}
    db_json = json.loads(json_util.dumps(src))
    resp_dict = dict(filter(lambda _: _[0] not in ban_dct, db_json.items()))
    return resp_dict


def db2dict_multi(src, ban_dct=None):
    """

    :param src: database result objects list
    :param ban_dct: forbidden keys
    :return:
    """
    resp_list = []
    if not ban_dct:
        ban_dct = {}
    if iter(src):
        resp_list = [db2dict(_, ban_dct) for _ in src]
    return resp_list


def add2list(src_list, adder):
    """
    Flatten adder of list
    Assume adder's depth is less than 2
    
    :param src_list: 
    :param adder: 
    :return: 
    """
    if isinstance(adder, str):
        src_list.append(adder)
    elif iter(adder):
        src_list.extend(adder)
    return src_list


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
        # return immediately, otherwise flag would be over written
        if flag is False:
            break
    return flag
