from flask import (
    Flask, request, jsonify, json, g, session, redirect,
)
from sgo.config import BaseConfig, DevConfig
from bson import json_util

# extensions
from sgo.extensions import (
    admin_interface, bcrypt, pm,
    token_auth, jwt_token, jwt_refresh,
    rc,
)

# modules
from sgo.user import user
from sgo.auth import auth
from sgo.store import store
from sgo.lbs import lbs
from sgo.rtm import rtm
from sgo.media import media

# admin views
from sgo.views.admin_views import UserView, TaskView, ProductView


def create_app(config=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    # register extensions before blueprints
    # especially flask_restful
    register_blueprints(app)
    register_errorhandlers(app)

    @app.route('/test_redis')
    def test_redis():
        rc.flushdb()
        rc.rpush('a', '1')
        rc.rpush('a', '2')
        return jsonify(key=rc.lrange('a', 0, -1))

    @app.route('/show_db')
    def show_db():
        users = pm.db.users.find({'name': '绯村剑心'})
        return json_util.dumps(users)

    @app.route('/test_token')
    @token_auth.login_required
    def test_token():
        return 'Hello, %s' % g.current_user

    return app


def register_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = pm
    return db


def init_admin(admin):
    admin.add_view(UserView(pm.db.users))
    admin.add_view(TaskView(pm.db.tasks))
    admin.add_view(ProductView(pm.db.products))


def register_extensions(app):
    bcrypt.init_app(app)
    pm.init_app(app, config_prefix=BaseConfig.PYMONGO_CONFIG_PREFIX)

    admin_interface.init_app(app)
    with app.app_context():
        # within this block, current_app points to app.
        register_db()
        init_admin(admin_interface)


def register_blueprints(app):
    app.register_blueprint(user, url_prefix='/users')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(store)
    app.register_blueprint(lbs, url_prefix='/lbs')
    app.register_blueprint(rtm, url_prefix='/rtm')
    app.register_blueprint(media, url_prefix='/media')


def register_errorhandlers(app):
    pass

