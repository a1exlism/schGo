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
    if request.method == 'GET':
        name = request.args.get('name')
        school = request.args.get('school')
        return jsonify(name=name, school=school)
    elif request.method == 'POST':
        return 'resp from post'


@user.route('/<user_id>', methods=['GET', 'POST', 'PUT'])
def user_specific(user_id):
    if request.method == 'GET':
        return 'resp from get, ' + user_id
    elif request.method == 'POST':
        return 'resp from post, ' + user_id
    elif request.method == 'PUT':
        return 'resp from put, ' + user_id


@user.route('/me')
def user_me():
    if request.method == 'GET':
        return 'resp from get'


@user.route('/<user_id>/refresh_session_token')
def refresh_session_token(user_id):
    if request.method == 'PUT':
        return 'user refresh token, ' + user_id


@user.route('/<user_id>/update_pw')
def update_pw(user_id):
    if request.method == 'PUT':
        return 'resp from put, ' + user_id


@user.route('/login')
def user_login():
    if request.method == 'POST':
        return 'resp from user_login post'
