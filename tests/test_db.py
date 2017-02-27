# -*- coding: utf-8 -*-
import pytest
from sgo.user.models import User
from sgo.store.models import Task, Product


@pytest.mark.usefixtures('db')
class TestDatabase():
    def test_users(self, db):
        init_users(db)
        init_tasks(db)
        init_product(db)
        # clear_users(db)


def test_db(db):
    users = db.users.find()
    assert users


def init_users(db):
    coll = db.users
    if not coll.find_one({'id': 'test_user'}):
        test_user = User()
        test_user.doc['id'] = 'test_user'
        test_user.doc['name'] = '裴仲'
        test_user.doc['pw'] = '123456'
        coll.insert_one(test_user.doc)


def init_tasks(db):
    coll = db.tasks
    test_user = db.users.find_one({'id': 'test_user'})

    if not coll.find_one():
        test_task = Task()
        test_task.doc['publisher']['id'] = test_user._id
        coll.insert_one(test_task.doc)


def init_product(db):
    coll = db.products
    test_user = db.users.find_one({'id': 'test_user'})

    if not coll.find_one():
        test_product = Product()
        test_product.doc['publisher']['id'] = test_user._id
        coll.insert_one(test_product.doc)


def clear_users(db):
    coll = db.users
    coll.delete_many()
