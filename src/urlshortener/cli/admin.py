import click

import urlshortener.application


@click.group()
def cli():
    pass


@cli.group()
def db():
    pass


@db.command()
def create():
    with urlshortener.application.session_scope as session:
        session.create_all()


@db.command()
def drop():
    urlshortener.application.Base.metadata.drop_all()
    # urlshortener.application.db.drop_all()
