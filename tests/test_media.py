# -*- coding: utf-8 -*-
import pytest


@pytest.mark.usefixtures('app')
@pytest.mark.usefixtures('client')
@pytest.mark.usefixtures('db')
@pytest.mark.usefixtures('base_dir')
class TestImgUpload():
    def test_upload(self, client, base_dir):
        import os
        from io import BytesIO
        with open(os.path.join(base_dir, 'tests', 'res', 'flux_sq.png'),
                  'rb') as f:
            res = client.post('/media/img', data={
                'img': (BytesIO(f.read()), 'flux.png')
            })
        print(res.data)
        assert b'saved' in res.data


