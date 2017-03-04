# -*- coding: utf-8 -*-

from flask import (
    request, redirect, url_for, g, session, jsonify
)

# utils
from sgo.views.utils import b2json

# extensions
from sgo.extensions import pm

# modules
from sgo.user.models import User as UserModel
from sgo.user import user


@user.route('/', methods=['GET', 'POST'])
def user_index():
    """
    GET:    search user by name or school
    POST:   user login
    :return:
    """
    if request.method == 'GET':
        name = request.args.get('name')
        school = request.args.get('school')
        return jsonify(name=name, school=school)
    elif request.method == 'POST':
        return 'resp from post'


@user.route('/<user_id>', methods=['GET', 'PUT'])
def user_specific(user_id):
    """
    GET:    get user by id
    PUT:    update user
    :param user_id:
    :return:
    """
    if request.method == 'GET':
        return 'resp from get, ' + user_id
    elif request.method == 'POST':
        return 'resp from post, ' + user_id
    elif request.method == 'PUT':
        return 'resp from put, ' + user_id


@user.route('/me', methods=['GET'])
def user_me():
    """
    GET:    get current user by session token
    :return:
    """
    if request.method == 'GET':
        return 'resp from get'


@user.route('/<user_id>/refresh_session_token', methods=['PUT'])
def refresh_session_token(user_id):
    """
    PUT:    as the name
    :param user_id:
    :return:
    """
    if request.method == 'PUT':
        return 'user refresh token, ' + user_id


@user.route('/<user_id>/update_pw', methods=['PUT'])
def update_pw(user_id):
    """
    PUT:    as the name
    :param user_id:
    :return:
    """
    if request.method == 'PUT':
        return 'resp from update_pw , ' + user_id
