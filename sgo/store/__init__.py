# -*- coding: utf-8 -*-

from flask import Blueprint

store = Blueprint('store', __name__)

import sgo.store.views