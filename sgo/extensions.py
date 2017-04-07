# -*- coding: utf-8 -*-
""" Add flask extensions here
"""

from redis import Redis

from .config import BaseConfig

rc = Redis(decode_responses=True, db=0)

from flask_login import LoginManager

login_manager = LoginManager()

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

from flask_pymongo import PyMongo

pm = PyMongo()

from flask_admin import Admin
from .views.admin_views import SgoAdminIndexView

admin_interface = Admin(name=BaseConfig.SITE_NAME, template_mode='bootstrap3',
                        index_view=SgoAdminIndexView())

from flask_httpauth import HTTPTokenAuth

token_auth = HTTPTokenAuth(scheme=BaseConfig.TOKEN_AUTH_SCHEME)

from itsdangerous import TimedJSONWebSignatureSerializer as JWT

jwt_token = JWT(BaseConfig.TOKEN_SECRET_KEY,
                expires_in=BaseConfig.TOKEN_EXPIRES_TIME)
jwt_refresh = JWT(BaseConfig.TOKEN_SECRET_KEY,
                  expires_in=BaseConfig.TOKEN_REFRESH_EXPIRES_TIME)
