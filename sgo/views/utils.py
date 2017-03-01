# -*- coding: utf-8 -*-

from flask import json
from bson import json_util


def b2json(src):
    return json.loads(json_util.dumps(src))
