# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='session')
def base_dir():
    """ Get Project Base Directory
    :return: /.../sgo_python
    """
    import os
    print(os.getcwd())
    return os.getcwd()


@pytest.fixture(scope='session')
def app(request):
    from sgo import create_app
    from sgo.config import TestConfig
    app = create_app(TestConfig)
    return app


@pytest.fixture(scope='session')
def client(request, app):
    client = app.test_client()
    return client


@pytest.fixture(scope='session')
def db(request, app):
    with app.app_context():
        from sgo.extensions import pm
        db = pm.db
    return db


# @pytest.fixture(scope="function", autouse=True)
def divider_function(request):
    print('\n        --- function %s() start ---' % request.function.__name__)

    def fin():
        print('        --- function %s() done ---' % request.function.__name__)

    # to free function
    request.addfinalizer(fin)


# @pytest.fixture(scope="module", autouse=True)
def divider_module(request):
    print('\n    ------- module %s start ---------' % request.module.__name__)

    def fin():
        print('    ------- module %s done ---------' % request.module.__name__)

    request.addfinalizer(fin)


# @pytest.fixture(scope="session", autouse=True)
def divider_session(request):
    print('\n----------- session start ---------------')

    def fin():
        print('----------- session done ---------------')

    request.addfinalizer(fin)
