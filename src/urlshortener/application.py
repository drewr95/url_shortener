import os
import random
import string

import flask
import flask_sqlalchemy
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests

page_blueprint = flask.Blueprint('page_blueprint', __name__)
Base = declarative_base()
Session = sessionmaker()


def createApp():
    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.register_blueprint(page_blueprint)
    engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    Session.configure(bind=engine)
    return app


class Pair(Base):
    __tablename__ = 'pair'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence('user_id_seq'), primary_key=True)
    short = sqlalchemy.Column(sqlalchemy.String, unique=True)
    long = sqlalchemy.Column(sqlalchemy.String)


short_characters = string.ascii_letters + string.digits


def create_short():
    return ''.join(random.choices(short_characters, k=5))


def getURL(url: str):
    """
    adds the proper http(s) prefix to the url if it doesn't already exist
    :param url: url string to be checked
    :return: proper url path
    """
    if "http" not in url:
        if "www" not in url:
            url = "http://www." + url
        else:
            url = "http://" + url

    return requests.get(url).url


@page_blueprint.route('/')
def hello():
    return flask.jsonify("Hello World!")


@page_blueprint.route('/add', methods=['POST'])
def add():
    attempts = 42
    session = Session()

    for attempt in range(attempts):
        short = create_short()

        pair = Pair(
            short=short,
            long=flask.request.headers['long'],
        )
        pair.long = getURL(url=pair.long)
        session.add(pair)

        try:
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            if attempt < attempts:
                continue

            raise

        break

    return flask.jsonify(short=short)


@page_blueprint.route('/get/<short>')
def get(short):
    pair = Pair.query.filter_by(short=short).first()

    return flask.jsonify(long=pair.long)


@page_blueprint.route('/<short>')
def redirect(short):
    pair = Pair.query.filter_by(short=short).first()

    return flask.redirect(pair.long)
