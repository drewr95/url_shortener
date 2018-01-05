import os
from contextlib import contextmanager

import flask
import urlshortener.url
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

page_blueprint = flask.Blueprint('page_blueprint', __name__)
engine = sqlalchemy.create_engine(os.environ['DATABASE_URL'])
Base = sqlalchemy.ext.declarative.declarative_base(bind=engine)
Session = sqlalchemy.orm.sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = sqlalchemy.orm.scoped_session(Session)

    try:
        yield session
        session.commit()
    except:
        raise

def createApp():
    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.register_blueprint(page_blueprint)
    return app


class Pair(Base):
    __tablename__ = 'pair'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence('id'), primary_key=True)
    short = sqlalchemy.Column(sqlalchemy.String, unique=True)
    long = sqlalchemy.Column(sqlalchemy.String)


@page_blueprint.route('/')
def hello():
    return flask.jsonify('Hello World!')


@page_blueprint.route('/add', methods=['POST'])
def add():
    attempts = 42

    for attempt in range(attempts):

        pair = Pair(
            short=urlshortener.url.create_short(),
            long=flask.request.headers['long'],
        )
        pair.long = urlshortener.url.getURL(url=pair.long)
        with session_scope() as session:
            session.add(pair)

        break;
        # try:
        #     # session.commit()
        # except sqlalchemy.exc.IntegrityError:
        #     if attempt < attempts:
        #         continue
        #
        #     raise
        #
        # break

    return flask.jsonify(short=pair.short)


@page_blueprint.route('/get/<short>')
def get(short):
    with session_scope() as session:
        pair = session.query(Pair).filter_by(short=short).first()
        return flask.jsonify(long=pair.long)


@page_blueprint.route('/<short>')
def redirect(short):
    with session_scope() as session:
        pair = session.query(Pair).filter_by(short=short).first()
        return flask.redirect(pair.long)
