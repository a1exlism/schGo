# -*- coding: utf-8 -*-
"""Views for sgo
Based on flask-admin and flask-login
"""

# flask
from flask import (
    request, redirect, url_for, flash, g,
    render_template, json
)

# extensions
from flask_admin import (
    Admin, AdminIndexView, expose, helpers
)
from flask_admin.contrib.pymongo import ModelView, filters
from flask_admin.model.fields import InlineFormField, InlineFieldList
from flask_admin.base import MenuLink
import flask_login

# modules
from ..models import Admin
from ..config import BaseConfig
from .admin_form import (
    # Custom Fields
    ObjectIdField,
    # Basic Custom Form

    # Derived Custom Form
)
# utils
from wtforms import form, validators

from wtforms.fields import (
    StringField, IntegerField, TextAreaField,
    PasswordField, DateTimeField, FileField
)
from bson import json_util


class AdminLoginForm(form.Form):
    username = StringField('username', validators=[validators.required()])
    password = PasswordField('password', validators=[validators.required()])

    def validate_login(self, field):
        admin = self.get_admin()

        if admin is None:
            raise validators.ValidationError('Invalid admin')

        if self.password.data != admin.password:
            raise validators.ValidationError("Invalid password")

    @staticmethod
    def get_admin(id=None):
        # TODO: find a better way to get Admin, store admin in db
        # admin = getattr(g, 'admin', None)
        # if admin is None:
        #     g.admin = Admin()
        # return g.admin
        return Admin()


class SgoAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return True

    @expose('/')
    def index(self):
        if not flask_login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return self.render('admin/index.html',
                           current_user=flask_login.current_user)

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = AdminLoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            admin = form.get_admin(request.form['username'])
            form.validate_login(form.password)
            flask_login.login_user(admin)
            flash('Login successfully')

        if flask_login.current_user.is_authenticated:
            return redirect(url_for('.index'))

        self._template_args['form'] = form
        return super().index()

    @expose('/logout/')
    def logout_view(self):
        flask_login.logout_user()
        g.admin = None
        return redirect(url_for('.index'))


class SgoModelView(ModelView):
    """
    Base of All SGO admin model view
    """

    page_size = 50

    def is_accessible(self):
        return flask_login.current_user.is_authenticated


class UserForm(form.Form):
    _id = ObjectIdField('object_id')
    id = StringField('id')
    pw = StringField('pw')
    name = StringField('name')
    email = StringField('email')
    phone = StringField('phone')

    bio = StringField('bio')
    school = StringField('school')
    avatar_url = StringField('avatar_url')
    qq = StringField('qq')
    weibo = StringField('weibo')
    wechat = StringField('wechat')
    balance = IntegerField('balance')
    credit = IntegerField('credit')
    tasks = InlineFieldList(ObjectIdField('tasks'))


class UserView(SgoModelView):
    column_list = ['_id', 'id', 'pw', 'name', 'email', 'phone',
                   'bio', 'school', 'avatar_url', 'qq', 'weibo', 'wechat',
                   'balance', 'credit', 'tasks']
    form = UserForm


class PublisherEmbed(form.Form):
    id = ObjectIdField('id')
    name = StringField('name')
    avatar_url = StringField('avatar_url')


class CommentEmbed(form.Form):
    floor = IntegerField('floor')
    author = StringField('author')
    author_id = ObjectIdField('author_id')
    content = TextAreaField('content')
    likes = IntegerField('likes')


class TagsEmbed(form.Form):
    tag = StringField('tag')


class ProductParamsEmbed(form.Form):
    pic_url = InlineFieldList(StringField('pic_url'))
    video_url = InlineFieldList(StringField('video_url'))
    views = IntegerField('views')
    likes = IntegerField('likes')


class TaskForm(form.Form):
    place = StringField('place')
    publisher = InlineFormField(PublisherEmbed)
    receiver_id = StringField('receiver_id')
    desc = StringField('desc')
    reward = IntegerField('reward')
    pub_time = DateTimeField('pub_time')
    # from is builtin keyword
    from_ = StringField('from')
    to = StringField('to')

    tags = InlineFieldList(StringField(TagsEmbed))

    comments = InlineFieldList(InlineFormField(CommentEmbed))


class TaskView(SgoModelView):
    column_list = ['place', 'publisher',
                   'receiver_id', 'desc',
                   'reward', 'pub_time',
                   'from_', 'to_', 'tags', 'comments']

    form = TaskForm

    def get_list(self, *args, **kwargs):
        count, data = super(TaskView, self).get_list(*args, **kwargs)
        for item in data:
            item['publisher'] = json.loads(json_util.dumps(item['publisher']))
            item['comments'] = json.loads(json_util.dumps(item['comments']))

        return count, data


class ProductForm(form.Form):
    publisher = InlineFormField(PublisherEmbed)
    pub_time = DateTimeField('pub_time')
    desc = StringField('desc')
    params = InlineFormField(ProductParamsEmbed)
    tags = InlineFieldList(StringField(TagsEmbed))
    comments = InlineFieldList(InlineFormField(CommentEmbed))


class ProductView(SgoModelView):
    column_list = ['publisher', 'pub_time', 'desc',
                   'params', 'tags', 'comments']

    form = ProductForm

    def get_list(self, *args, **kwargs):
        count, data = super(ProductView, self).get_list(*args, **kwargs)
        for item in data:
            item['publisher'] = json.loads(json_util.dumps(item['publisher']))
            item['comments'] = json.loads(json_util.dumps(item['comments']))

        return count, data


class AuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return flask_login.current_user.is_authenticated


class NotAuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return not flask_login.current_user.is_authenticated


def init_admin_views(admin):
    """Init flask_admin
    Called in register_extensions in sgo/__init__.py
    :return flask-admin instance
    """
    conn = g.database
    admin.add_link(MenuLink(name='Back Home', url='/admin'))
    admin.add_link(NotAuthenticatedMenuLink(name='Login', url='/admin/login'))
    admin.add_link(AuthenticatedMenuLink(name='Logout', url='/admin/logout'))
    admin.add_view(UserView(conn.db.users))
    admin.add_view(TaskView(conn.db.tasks))
    admin.add_view(ProductView(conn.db.products))
