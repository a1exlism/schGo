# -*- coding: utf-8 -*-

from sgo import create_app, config

# TODO: switch the config mode when deploy
app = create_app(config=config.DevConfig)

if __name__ == '__main__':
    with app.app_context():
        app.run(host='0.0.0.0')
