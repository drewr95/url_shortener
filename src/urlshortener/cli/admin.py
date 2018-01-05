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
    urlshortener.application.Base.metadata.create_all()


@db.command()
def drop():
    urlshortener.application.Base.metadata.drop_all()
