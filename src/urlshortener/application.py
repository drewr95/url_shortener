import os
import flask
import urlshortener.url
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import urlshortener.database

page_blueprint = flask.Blueprint('page_blueprint', __name__)

def createApp():
    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.register_blueprint(page_blueprint)
    urlshortener.database.db.init_app(app)
    return app


@page_blueprint.route('/')
def hello():
    return flask.jsonify('Hello World!')


@page_blueprint.route('/add', methods=['POST'])
def add():
    attempts = 42

    for attempt in range(attempts):

        pair = urlshortener.database.Pair(
            short=urlshortener.url.create_short(),
            long=flask.request.headers['long'],
        )
        pair.long = urlshortener.url.getURL(url=pair.long)
        urlshortener.database.db.add(pair)

        try:
            urlshortener.database.db.commit()
        except sqlalchemy.exc.IntegrityError:
            if attempt < attempts:
                continue

            raise

        break

    return flask.jsonify(short=pair.short)


@page_blueprint.route('/get/<short>')
def get(short):
    pair = urlshortener.database.Pair.query.filter_by(short=short).first()
    return flask.jsonify(long=pair.long)


@page_blueprint.route('/<short>')
def redirect(short):
    pair = urlshortener.database.Pair.query.filter_by(short=short).first()
    return flask.redirect(pair.long)
