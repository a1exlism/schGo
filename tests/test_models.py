# -*- coding: utf-8 -*-
import pytest
from sgo.user.models import User
from sgo.store.models import Task, Product


@pytest.mark.usefixtures('db')
@pytest.mark.usefixtures('app')
@pytest.mark.usefixtures('client')
class TestModels():
    pass
