# -*- coding: utf-8 -*-

# extensions

from flask_admin.contrib.pymongo import ModelView, filters
from flask_admin.model.fields import InlineFormField, InlineFieldList

from wtforms import form
from wtforms.fields import StringField, IntegerField, TextAreaField


class UserForm(form.Form):
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
    tasks = TextAreaField('tasks')


class UserView(ModelView):
    column_list = ['id', 'pw', 'name', 'email', 'phone',
                   'bio', 'school', 'avatar_url', 'qq', 'weibo', 'wechat',
                   'balance', 'credit', 'tasks']
    form = UserForm


class TaskForm(form.Form):
    place = StringField('place')
    publisher = TextAreaField('publisher')
    receiver_id = StringField('receiver_id')
    desc = StringField('desc')
    reward = IntegerField('reward')
    pub_time = StringField('pub_time')
    # from is builtin keyword
    from_ = TextAreaField('from')
    to = TextAreaField('to')


class TaskView(ModelView):
    column_list = ['place', 'publisher', 'receiver_id', 'desc',
                   'reward', 'pub_time', 'from_', 'to']

    form = TaskForm


class ProductForm(form.Form):
    publisher = StringField('publisher')
    pub_time = StringField('pub_time')
    desc = StringField('desc')
    params = TextAreaField('params')
    tags = StringField('tags')
    comments = TextAreaField('comments')


class ProductView(ModelView):
    column_list = ['publisher', 'pub_time', 'desc',
                   'params', 'tags', 'comments']

    form = ProductForm
