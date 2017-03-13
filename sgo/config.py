# -*- coding: utf-8 -*-
"""All config options of schGo"""

import os
from sgo.instance import config
from bson.json_util import JSONOptions
from datetime import timedelta
import os

BASEDIR = os.getcwd()


class BaseConfig(object):
    """Default configuration options."""
    SITE_NAME = 'School GO'

    SECRET_KEY = config.SECRET_KEY_INSTANCE
    AES_IV = config.AES_IV_INSTANCE

    MONGO_DBNAME = 'schgo'

    # for jsonify
    JSON_SORT_KEYS = False

    JSON_AS_ASCII = False

    # for flask-pymongo
    PYMONGO_CONFIG_PREFIX = 'MONGO'

    # admin white list
    ADMIN_LIST = ['admin']
    ADMIN_PW = config.ADMIN_PW

    "auth module"
    COOKIE_DURATION = timedelta(days=365)
    TOKEN_AUTH_SCHEME = 'sgo_token'
    TOKEN_SECRET_KEY = config.TOKEN_SECRET_KEY_INSTANCE
    TOKEN_REFRESH_KEY = config.TOKEN_REFRESH_KEY_INSTANCE
    # in seconds
    TOKEN_EXPIRES_TIME = 3600 * 24 * 365
    # TODO: add token refresh
    TOKEN_REFRESH_EXPIRES_TIME = 15

    "file uploads"
    # TODO: change this when deploy
    UPLOAD_FOLDER = os.path.join(BASEDIR, 'sgo', 'media_storage')
    PIC_ALLOWED_EXTENSIONS = ('jpg', 'jpeg', 'png', 'bmp')


class DevConfig(BaseConfig):
    """Development configuration options"""
    DEBUG = True
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False


class TestConfig(BaseConfig):
    """Testing configuration options."""
    TESTING = True
    WTF_CSRF_ENABLED = False
