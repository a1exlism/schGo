# -*- coding: utf-8 -*-

from flask import (
    request, redirect, url_for, g, session
)

from flask_restful import Resource, Api
from flask import jsonify, json
from bson import json_util

# extensions
from sgo.extensions import pm

# modules
from sgo.user.models import User as UserModel


class User(Resource):
    def get(self):
        user = pm.db.users.find()
        return jsonify(json.loads(json_util.dumps(user)))


class TestUser(Resource):
    """Test api class

    """
    user_doc = UserModel()

    def get(self):
        users = pm.db.users.find({'name': 'kitty'})
        return jsonify(json.loads(json_util.dumps(users)))


class TestLogin(Resource):
    pass


def register_user_apis(api):
    api.add_resource(User, '/')
    api.add_resource(TestUser, '/test_user')
