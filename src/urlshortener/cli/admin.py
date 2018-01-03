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
    urlshortener.application.db.create_all()


@db.command()
def drop():
    urlshortener.application.db.drop_all()
