# -*- coding: utf-8 -*-
import pytest
from sgo.user.models import User
from sgo.store.models import Task, Product


@pytest.mark.usefixtures('db')
@pytest.mark.usefixtures('app')
@pytest.mark.usefixtures('client')
class TestModels():
    def test(self):
        u1 = User()
        u1.doc['_id'] = '123123123'
        u2 = User()
        # pass if doc is not a value of class User
        assert '_id' not in u2.doc, 'value error'


def test_object_id(db):
    u = db.users.find_one({'id': 'test_user'})
    oid = u.get('_id')
    oid_str = str(oid)
    assert isinstance(oid_str, str)
