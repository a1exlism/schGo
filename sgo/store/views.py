# -*- coding: utf-8 -*-

from flask import request, jsonify, json
from bson import json_util

# extensions
from sgo.extensions import pm

# modules
from sgo.store import store
from sgo.store.models import Task as TaskModel
from sgo.store.models import Product as ProductModel


@store.route('/tasks', methods=['GET', 'POST'])
def tasks_index():
    if request.method == 'GET':
        return 'resp from get'
    elif request.method == 'POST':
        return 'resp from post'


@store.route('/tasks/<task_id>', methods=['GET', 'PUT'])
def tasks_specific(task_id):
    if request.method == 'GET':
        return 'resp from get, ' + task_id
    elif request.method == 'PUT':
        return 'resp from put, ' + task_id


@store.route('/products', methods=['GET', 'POST'])
def products_index():
    if request.method == 'GET':
        return 'resp from get'
    elif request.method == 'POST':
        return 'resp from post'


@store.route('/products/<product_id>', methods=['GET', 'PUT'])
def products_specific(product_id):
    if request.method == 'GET':
        return 'resp from get, ' + product_id
    elif request.method == 'PUT':
        return 'resp from put, ' + product_id
