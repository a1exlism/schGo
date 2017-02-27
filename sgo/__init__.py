from flask import (
    Flask, request, jsonify, json, g, session, redirect,
    url_for,
)
from werkzeug.utils import secure_filename
import os
from sgo.config import BaseConfig, DevConfig
from bson import json_util

# extensions
from sgo.extensions import (
    api, admin_interface, bcrypt, pm,
    token_auth, jwt_token, jwt_refresh
)
from flask_restful import Resource, Api
from flask_admin.contrib.pymongo import ModelView

# modules
from sgo.user import user
from sgo.user.views import register_user_apis
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

    @app.route('/test')
    def test_db():
        return 'Hello from test'

    @app.route('/show_db')
    def show_db():
        users = pm.db.users.find({'name': '绯村剑心'})
        return json_util.dumps(users)

    users = ['john', 'susan']
    for user in users:
        token = jwt_token.dumps({'username': user})
        print('*** token for {}: {}\n'.format(user, token))

    @app.route('/test_token')
    @token_auth.login_required
    def test_token():
        return 'Hello, %s' % g.current_user

    @token_auth.verify_token
    def verify_token(token):
        g.current_user = None
        try:
            data = jwt_token.loads(token)
            print(data)
        except:
            return False
        if 'username' in data:
            g.current_user = data['username']
            return True
        return False

    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[
                   1].lower() in BaseConfig.PIC_ALLOWED_EXTENSIONS

    # @app.route('/file', methods=['GET', 'POST'])
    def upload_file_me():
        if request.method == 'POST':
            file = request.files['file']
            if not file:
                print('No file part')
                return 'no file part'
            # if user does not select file, browser alse
            # submit a empty part without filename
            if file.filename == '':
                print('No selected file')
                return 'no selected file'
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return 'file {} uploaded'.format(filename)
        elif request.method == 'GET':
            return 'method not allowed'

    @app.route('/file', methods=['GET', 'POST'])
    def upload_file():
        from flask import flash
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('static',
                                        filename=filename))
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        '''

    return app


def register_apis():
    # api from modules
    user_api = Api(user)
    register_user_apis(user_api)

    store_api = Api(store)
    register_user_apis(store_api)


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
    register_apis()
    api.init_app(app)

    bcrypt.init_app(app)

    pm.init_app(app, config_prefix=BaseConfig.PYMONGO_CONFIG_PREFIX)

    admin_interface.init_app(app)

    with app.app_context():
        # within this block, current_app points to app.
        register_db()
        init_admin(admin_interface)


def register_blueprints(app):
    app.register_blueprint(user, url_prefix='/user')

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(store)
    app.register_blueprint(lbs, url_prefix='/lbs')
    app.register_blueprint(rtm, url_prefix='/rtm')
    app.register_blueprint(media, url_prefix='/media')


def register_errorhandlers(app):
    pass


if __name__ == '__main__':
    create_app(DevConfig).run()
