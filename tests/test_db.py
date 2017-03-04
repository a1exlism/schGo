# -*- coding: utf-8 -*-
import pytest
from sgo.user.models import User
from sgo.store.models import Task, Product


@pytest.mark.usefixtures('db')
class TestDatabase():
    def test_users(self, db):
        mode = 'creat'
        if mode == 'create':
            init_users(db)
            init_tasks(db)
            init_product(db)
        else:
            clear_users(db)
            clear_tasks(db)
            clear_products(db)


def test_db(db):
    users = db.users.find()
    assert users


def init_users(db):
    coll = db.users
    user_dict = {
        'id': '',
        'name': '',
        'pw': '123456',
        'school': ''
    }

    def create_user(id_, name, school):
        if not coll.find_one({'id': id_}):
            resp = user_dict
            resp['id'] = id_
            resp['name'] = name
            resp['school'] = school
            temp_user = User()
            for _ in resp:
                temp_user.doc[_] = resp[_]
            if '_id' in temp_user.doc:
                del temp_user.doc['_id']
            coll.insert_one(temp_user.doc)

    create_user('test_user', '裴仲', '杭州电子科技大学')
    create_user('kitty', 'kitty', 'PKU')
    create_user('lucy', 'lucy', 'TSU')


def init_tasks(db):
    coll = db.tasks
    test_user = db.users.find_one({'id': 'test_user'})

    if not coll.find_one():
        test_task = Task()
        test_task.doc['publisher']['id'] = test_user['_id']
        coll.insert_one(test_task.doc)


def init_product(db):
    coll = db.products
    test_user = db.users.find_one({'id': 'test_user'})

    if not coll.find_one():
        test_product = Product()
        test_product.doc['publisher']['id'] = test_user['_id']
        coll.insert_one(test_product.doc)


def clear_users(db):
    coll = db.users
    coll.delete_many({})


def clear_tasks(db):
    coll = db.tasks
    coll.delete_many({})


def clear_products(db):
    coll = db.products
    coll.delete_many({})
