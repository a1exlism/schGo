# -*- coding: utf-8 -*-
import click

# modules
from sgo import create_app, config

# TODO: switch the config mode when deploy
app = create_app(config=config.DevConfig)

if __name__ == '__main__':
    with app.app_context():
        app.run(host='0.0.0.0')


@app.cli.command()
def initdb():
    click.echo('init the db')
