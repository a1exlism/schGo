# -*- coding: utf-8 -*-
import click

# modules
from sgo import create_app, config


def run_app():
    # TODO: switch the config mode when deploy
    app = create_app(config=config.DevConfig)
    with app.app_context():
        app.run(host='0.0.0.0')


if __name__ == '__main__':
    run_app()
