"""
Stem of SGO
"""
# flask
from flask import (
    Flask, request, jsonify, json, g, session, redirect,
    render_template, url_for,
)
from sgo.config import BaseConfig, DevConfig
from bson import json_util

# extensions
from sgo.extensions import (
    login_manager, bcrypt, admin_interface,
    pm, token_auth, jwt_token, jwt_refresh,
    rc,
)

# modules
from sgo.user import user
from sgo.auth import auth
from sgo.store import store
from sgo.lbs import lbs
from sgo.rtm import rtm
from sgo.media import media
from sgo.views.admin_views import init_admin_views
from sgo.models import Admin as AdminModel


def create_app(config=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route('/test_redis')
    def test_redis():
        rc.flushdb()
        rc.rpush('a', '1')
        rc.rpush('a', '2')
        return jsonify(key=rc.lrange('a', 0, -1))

    @app.route('/show_db')
    def show_db():
        users = pm.db.users.find({'name': '裴仲'})
        return json_util.dumps(users)

    @app.route('/test_token')
    @token_auth.login_required
    def test_token():
        return 'Hello, %s' % g.current_user

    @app.route('/test_file/<path:filename>')
    def get_upload(filename):
        return pm.send_file(filename)

    @app.route('/test_file/<path:filename>', methods=['POST'])
    def save_upload(filename):
        pm.save_file(filename, request.files['img'])
        return redirect(url_for('get_upload', filename=filename))

    @app.route('/init_db_for_test', methods=['GET'])
    def init_db_for_test():
        key = request.args.get('key')
        if key == 'hello':
            pass
        return jsonify(flag=1, msg='success')

    return app


def globalize_db(conn):
    """Called in register_extensions
    :return: db instance
    """
    db = getattr(g, 'database', None)
    if db is None:
        g.database = conn
    return db


def register_extensions(app):
    # flask-bcrypt
    bcrypt.init_app(app)

    # pymongo
    pm.init_app(app, config_prefix=BaseConfig.PYMONGO_CONFIG_PREFIX)

    # flask-login
    login_manager.init_app(app)

    # sgo_admin
    admin_interface.init_app(app)

    @login_manager.user_loader
    def load_admin(id):
        # admin = getattr(g, 'admin', None)
        # if admin is None:
        #     g.admin = AdminModel()
        return AdminModel()

    with app.app_context():
        globalize_db(pm)
        init_admin_views(admin_interface)


def register_blueprints(app):
    app.register_blueprint(user, url_prefix='/users')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(store)
    app.register_blueprint(lbs, url_prefix='/lbs')
    app.register_blueprint(rtm, url_prefix='/rtm')
    app.register_blueprint(media, url_prefix='/media')


def register_errorhandlers(app):
    pass
