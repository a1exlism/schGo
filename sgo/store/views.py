# -*- coding: utf-8 -*-

from flask import request, jsonify, g, json

# extensions
from sgo.extensions import pm, token_auth

# modules
from sgo.auth.views import is_login
from sgo.store import store
from sgo.store.models import Task as TaskModel
from sgo.store.models import Product as ProductModel

# utils
from sgo.utils import (
    db2dict, db2dict_multi, clean_str,
    add2list
)
from datetime import datetime


@store.route('/tasks', methods=['GET', 'POST'])
def tasks_index():
    """
    GET:    search tasks
    POST:   publish task
    :return:
    """
    if request.method == 'GET':
        """
        Search by key word
        """
        kw = request.args.get('kw')
        state, kw = clean_str(kw)
        if not state:
            return jsonify(flag=0, msg="search key error.")
        task_list = pm.db.tasks.find({"$or": [
            {"desc": {"$regex": kw}},
            {"tags": {"$regex": kw}}
        ]})
        return jsonify(flag=1, data=db2dict_multi(task_list))

    # TODO: add transactions
    elif request.method == 'POST':

        if not is_login():
            return jsonify(flag=0, msg='you are not login')
        place = request.form['place']
        publisher_id = g.current_user
        desc = request.form['desc']
        reward = int(request.form['reward'])
        if reward < 0:
            return jsonify(flag=0, msg='reward can\'t be negative')
        tags = request.form.get('tags', None)
        tags_list = tags.lstrip('[').rstrip(']').split(',')

        # dicts
        # 接受时并不序列化
        from_ = json.loads(request.form['from'])
        to_ = json.loads(request.form['to'])

        # this condition is useless actually
        if place and from_:
            t = TaskModel()
            publisher = pm.db.users.find_one({'id': publisher_id})
            publisher_doc = {
                'id': publisher_id,
                'name': publisher['name'],
                'avatar_url': publisher['avatar_url']
            }

            t.doc['place'] = place
            t.doc['publisher'] = publisher_doc
            t.doc['desc'] = desc
            t.doc['reward'] = reward
            t.doc['pub_time'] = datetime.utcnow()
            t.doc['from_'] = from_
            t.doc['to_'] = to_
            t.doc['tags'] = tags_list

            # 返回时内嵌的 dict 会序列化
            t.id = pm.db.tasks.insert_one(t.doc).inserted_id
            publisher.get('tasks').append(t.id)
            pm.db.users.find_one_and_update({'id': publisher_id},
                                            {'$push':
                                                {
                                                    'tasks': t.id
                                                }})
            return jsonify(flag=1, task_id=str(t.id))
        else:
            return jsonify(flag=0, msg='bad request')


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
        state, kw = clean_str(kw)
        if not state:
            return jsonify(flag=0, msg='search key error.')
        product_list = pm.db.products.find({"$or": [
            {"desc": {"$regex": kw}},
            {"tags": {"$regex": kw}}
        ]})
        return jsonify(flag=1, data=db2dict_multi(product_list))

    elif request.method == 'POST':
        if not is_login():
            return jsonify(flag=0, msg='you are not login')
        publisher_id = g.current_user
        price = int(request.form['price'])
        if price < 0:
            return jsonify(flag=0, msg='price value error')
        desc = request.form['desc']

        # they are lists
        pic_url = request.form['pic_url_list']
        video_url = request.form['video_url_list']

        tags = request.form.get('tags', None)
        tags_list = tags.lstrip('[').rstrip(']').split(',')

        p = ProductModel()
        publisher = pm.db.users.find_one({'id': publisher_id})
        publisher_doc = {
            'id': publisher_id,
            'name': publisher['name'],
            'avatar_url': publisher['avatar_url']
        }

        p.doc['publisher'] = publisher_doc
        p.doc['pub_time'] = datetime.utcnow()
        p.doc['price'] = price
        p.doc['desc'] = desc
        add2list(p.doc['pic_url'], pic_url)
        add2list(p.doc['video_url'], video_url)
        p.doc['tags'] = tags_list

        p.id = pm.db.tasks.insert_one(p.doc).inserted_id
        publisher.get('products').append(p.id)
        pm.db.users.find_one_and_update({'id': publisher_id},
                                        {'$push':
                                            {
                                                'tasks': p.id
                                            }})
        return jsonify(flag=1, product_id=str(p.id))
    else:
        return jsonify(flag=0, msg='bad request')


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
