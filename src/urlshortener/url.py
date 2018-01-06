import requests
import random
import string
import flask
import urlshortener.database_model
import sqlalchemy

short_characters = string.ascii_letters + string.digits
page_blueprint = flask.Blueprint('page_blueprint', __name__)


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
    return flask.jsonify('Hello World!')


@page_blueprint.route('/add', methods=['POST'])
def add():
    attempts = 42

    for attempt in range(attempts):

        pair = urlshortener.database_model.Pair(
            short=create_short(),
            long=flask.request.headers['long'],
        )
        pair.long = urlshortener.url.getURL(url=pair.long)
        urlshortener.database_model.db.session.add(pair)

        try:
            urlshortener.database_model.db_session.commit()
        except sqlalchemy.exc.IntegrityError:
            if attempt < attempts:
                continue

            raise

        break

    return flask.jsonify(short=pair.short)


@page_blueprint.route('/get/<short>')
def get(short):
    pair = urlshortener.database_model.Pair.query.filter_by(short=short).first()
    return flask.jsonify(pair.long)


@page_blueprint.route('/<short>')
def redirect(short):
    pair = urlshortener.database_model.Pair.query.filter_by(short=short).first()
    return flask.redirect(pair.long)
