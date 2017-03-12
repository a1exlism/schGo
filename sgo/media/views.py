# -*- coding: utf-8 -*-

from flask import jsonify, request, g
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from sgo.config import BaseConfig
from sgo.media import media

import os

from sgo.media import media

PIC_ALLOWED_EXTENSIONS = ('jpg', 'jpeg', 'png', 'bmp')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in PIC_ALLOWED_EXTENSIONS


@media.route('/img', methods=['GET', 'POST'])
def image_api():
    if request.method == 'GET':
        return 'response for GET'
    elif request.method == 'POST':
        if 'img' not in request.files:
            return jsonify(flag=0, msg='No img part')
        img = request.files['img']
        if img.filename == '':
            return jsonify(flag=0, msg='no selected file')
        if img and allowed_file(img.filename):
            filename = secure_filename(img.filename)
            img.save(os.path.join(BaseConfig.UPLOAD_FOLDER, filename))
            return jsonify(flag=1, msg='file saved')


@media.route('/test_img/<path:filename>', methods=['GET', 'POST'])
def image_api_mongo(filename):
    mongo = g.database
    assert mongo, 'get database failed'
    return jsonify(flag=1)
