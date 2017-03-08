# -*- coding: utf-8 -*-

from flask import request, jsonify, json
from bson import json_util

# extensions
from sgo.extensions import pm, token_auth

# modules
from sgo.auth.views import is_login
from sgo.store import store
from sgo.store.models import Task as TaskModel
from sgo.store.models import Product as ProductModel
from sgo.utils import db2dict, db2dict_multi


@store.route('/tasks', methods=['GET', 'POST'])
def tasks_index():
    """
    GET:    search tasks
    POST:   publish task
    :return:
    """
    if request.method == 'GET':
        kw = request.args.get('kw')
        return 'task resp for get'

    elif request.method == 'POST':

        if not is_login():
            return jsonify(flag=0, msg='you are not login')

        place = request.form['place']


@store.route('/tasks/<task_id>', methods=['GET', 'PUT'])
def tasks_specific(task_id):
    """
    GET:    get task by id
    PUT:    update task by id
    :param task_id:
    :return:
    """
    if request.method == 'GET':
        t_list = pm.db.tasks.find()
        task_id = db2dict_multi(t_list)[0].get('_id')
        t = pm.db.tasks.find_one({'_id': task_id})
        return jsonify(flag=1, id=task_id)
    elif request.method == 'PUT':
        return 'resp from put, ' + task_id


@store.route('/products', methods=['GET', 'POST'])
def products_index():
    """
    GET:    search products
    POST:   publish products
    :return:
    """
    if request.method == 'GET':
        kw = request.args.get('kw')
        return 'resp from get'
    elif request.method == 'POST':
        if not is_login():
            return jsonify(flag=0, msg='you are not login')
        return 'resp from post'


@store.route('/products/<product_id>', methods=['GET', 'PUT'])
def products_specific(product_id):
    """
    GET:    get product by id
    PUT:    update product by id
    :param product_id:
    :return:
    """
    if request.method == 'GET':
        return 'resp from get, ' + product_id
    elif request.method == 'PUT':
        return 'resp from put, ' + product_id
