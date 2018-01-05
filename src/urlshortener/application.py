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
    engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    urlshortener.database.db_session = sqlalchemy.orm.scoped_session(sqlalchemy.orm.sessionmaker(bind=engine))
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
        urlshortener.database.db_session.add(pair)

        try:
            urlshortener.database.db_session.commit()
        except sqlalchemy.exc.IntegrityError:
            if attempt < attempts:
                continue

            raise

        break

    return flask.jsonify(short=pair.short)


@page_blueprint.route('/get/<short>')
def get(short):
    pair = urlshortener.database.Pair.query.filter_by(short=short).first()
    return flask.jsonify(pair.long)


@page_blueprint.route('/<short>')
def redirect(short):
    pair = urlshortener.database.Pair.query.filter_by(short=short).first()
    return flask.redirect(pair.long)
