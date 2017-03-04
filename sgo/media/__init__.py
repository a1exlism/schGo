# -*- coding: utf-8 -*-

from flask import Blueprint

media = Blueprint('media', __name__)

import sgo.media.views
