# -*- coding: utf-8 -*-
import pytest


@pytest.mark.usefixtures('app')
@pytest.mark.usefixtures('client')
@pytest.mark.usefixtures('db')
class TestUrlConverter():
    def test_bson_object_id_converter(self):
        from bson import ObjectId
        from flask.ext.pymongo import BSONObjectIdConverter

        converter = BSONObjectIdConverter("/")
        assert converter.to_python("4e4ac5cfffc84958fa1f45fb") == \
               ObjectId("4e4ac5cfffc84958fa1f45fb")
        assert converter.to_url(ObjectId("4e4ac5cfffc84958fa1f45fb")) == \
               "4e4ac5cfffc84958fa1f45fb"


def init_user_db():
    pass


class TestSGO(object):
    def test_hello(self, client):
        resp = client.get('/test')
        assert resp


def test_chech_list():
    ori = {
        'params': {
            'key_1': 'value_1',
            'key_2': 'value_2'
        },
        'tags': ['233', 'fun'],
        'users': [
            {'id': '1'}
        ]

    }

    test = {
        'params': {
            'key_1': 'value_1',
            'key_2': 'value_2'
        },
        'tags': ['233', 'fun', 'sb'],
        'users': [
            {'id': '1'},
            {'id': '2'},
            {'id': '3',
             'balance': 5}
        ]
    }
    from sgo.utils import check_dict
    assert not check_dict(test, ori)
