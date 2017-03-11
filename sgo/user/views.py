# -*- coding: utf-8 -*-

from flask import (
    request, redirect, url_for, g, session,
    jsonify, json
)

# utils
from bson import json_util

# extensions
from sgo.extensions import pm, token_auth

# modules
from sgo.user.models import User as UserModel
from sgo.user import user
from sgo.utils import (
    db2dict, db2dict_multi, check_id
)


@user.route('', methods=['GET', 'POST'])
def user_index():
    """
    GET:    search user by name
    POST:   user register
    :return:
    """
    ban_dct = {
        'pw', 'email', 'phone',
        'qq', 'weibo', 'wechat', 'balance', 'credit', 'tasks'
    }

    if request.method == 'GET':
        name = request.args.get('name')
        if name:
            u = pm.db.users.find({'name': name})
            user_list = db2dict_multi(u, ban_dct)
            return jsonify(flag=1, data=user_list)
        else:
            return jsonify(flag=0, msg='user not find')

    elif request.method == 'POST':
        input_id = request.form['id']
        if not check_id(input_id):
            return jsonify(flag=0, msg='id not allowed.')
        pw = request.form['pw']
        phone = request.form['phone']
        school = request.form['school']
        if input_id and pw and phone and school:
            u = UserModel()
            u.doc['id'], u.doc['pw'], u.doc['phone'], u.doc['school'] = \
                input_id, pw, phone, school
            u.doc['name'] = input_id
            if pm.db.users.find({'id': input_id}).count():
                return jsonify(flag=0, msg='user %s ready exist.')
            pm.db.users.insert_one(u.doc)
            return jsonify(flag=0, msg='register success.')


@user.route('/<user_id>', methods=['GET', 'PUT'])
@token_auth.login_required
def user_specific(user_id):
    """
    GET:    get user by id
    PUT:    update user
    :param user_id:
    :return:
    """
    ban_dct = ['pw', 'email', 'phone',
               'qq', 'weibo', 'wechat', 'balance', 'credit', 'tasks']
    if request.method == 'GET':
        if user_id != g.current_user:
            return jsonify(flag=0, msg='user do not match')
        if user_id:
            u = pm.db.users.find({'id': user_id})
            resp = db2dict(u, ban_dct)
            return jsonify(flag=1, data=resp)
        else:
            return jsonify(flag=0, msg='user do not exist.')

    elif request.method == 'PUT':
        "Request should contain all the fields list blow"
        # TODO: find a better way to do this
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        bio = request.form['bio']
        school = request.form['school']
        avatar_url = request.form['avatar_url']
        qq = request.form['qq']
        weibo = request.form['weibo']
        wechat = request.form['wechat']

        check_list = [name, email, phone, bio, school,
                      avatar_url, qq, weibo, wechat]

        for _ in check_list:
            if not _:
                return jsonify(flag=0)

        pm.db.users.find_one_and_update({'id': g.current_user},
                                        {'$set':
                                            {
                                                'name': name,
                                                'email': email,
                                                'phone': phone,
                                                'bio': bio,
                                                'school': school,
                                                'avatar_url': avatar_url,
                                                'qq': qq,
                                                'weibo': weibo,
                                                'wechat': wechat
                                            }
                                        })
        return jsonify(flag=1, msg='update success')


@user.route('/me', methods=['GET'])
@token_auth.login_required
def user_me():
    """
    GET:    get current user by session token
    :return:
    """
    ban_dct = ['pw']
    if request.method == 'GET':
        try:
            user_id = g.current_user
        except Exception:
            return jsonify(flag=0)
        else:
            u = pm.db.users.find_one({'id': user_id})
            resp_dict = db2dict(u, ban_dct)
            return jsonify(flag=1, data=resp_dict)


@user.route('/<user_id>/update_pw', methods=['PUT'])
@token_auth.login_required
def update_pw(user_id):
    """
    PUT:    as the name
    :param user_id:
    :return:
    """
    if request.method == 'PUT':
        if user_id != g.current_user:
            return jsonify(flag=0)
        u = pm.db.users.find_one({'id': g.current_user})
        pw_server = u['pw']
        pw_input = request.form['pw']
        new_pw = request.form['new_pw']
        if pw_input != pw_server:
            return jsonify(flag=0, msg='password mismatch')
        else:
            pm.db.users.find_one_and_update({'id': g.current_user},
                                            {'$set':
                                                {
                                                    'pw': new_pw
                                                }
                                            })
            return jsonify(flag=1)
