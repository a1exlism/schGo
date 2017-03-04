# -*- coding: utf-8 -*-

# flask
from flask import request, g, jsonify

# extensions
from sgo.extensions import pm, token_auth, jwt_token

# modules
from sgo.auth import auth


@auth.route('/login', methods=['POST'])
def login():
    """
    POST:   user login by id and pw
    :return: json with token
    """
    if request.method == 'POST':
        user_id = request.form['id']
        user = pm.db.users.find_one({'id': user_id})
        pw = request.form['pw']
        if pw == user['pw']:
            flag, token = 1, jwt_token.dumps({'username': user_id})
        else:
            flag, token = 0, ''
        return jsonify(flag=flag, token=token)


@auth.route('/<user_id>/refresh_session_token', methods=['PUT'])
def refresh_session_token(user_id):
    """
    PUT:    as the function name
    :param user_id:
    :return:
    """
    if request.method == 'PUT':
        return jsonify(flag=0, new_token='new token')


# @token_auth.verify_token
# TODO: uncomment this when deploy
def verify_token(token):
    """
    Get Token From 'Authorization' in Header
    :param token: config.TOKEN_AUTH_SCHEME TokenString
    :return:
    """
    g.current_user = None
    try:
        data = jwt_token.loads(token)
    except IOError:
        return False

    if 'username' in data:
        g.current_user = data['username']
        return True
    return False


@token_auth.verify_token
def verify_token_dev(token):
    g.current_user = 'test_user'
    return True
