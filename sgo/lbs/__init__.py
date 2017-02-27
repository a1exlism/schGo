# -*- coding: utf-8 -*-

from flask import Blueprint

lbs = Blueprint('lbs', __name__)

import sgo.lbs.views