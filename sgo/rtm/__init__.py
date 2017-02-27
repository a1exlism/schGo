# -*- coding: utf-8 -*-

from flask import Blueprint

rtm = Blueprint('rtm', __name__)

import sgo.rtm.views