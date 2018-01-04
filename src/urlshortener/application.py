import os
import random
import string

import flask
import flask_sqlalchemy
import sqlalchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = flask_sqlalchemy.SQLAlchemy(app)


class Pair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String, unique=True)
    long = db.Column(db.String)


short_characters = string.ascii_letters + string.digits


def create_short():
    return ''.join(random.choices(short_characters, k=5))


def add_prefix(url: str):
    if "http" not in url:
        if "www" not in url:
            url = "http://www." + url
        else:
            url = "http://" + url

    return url


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/add', methods=['POST'])
def add():
    attempts = 42

    for attempt in range(attempts):
        short = create_short()

        pair = Pair(
            short=short,
            long=flask.request.headers['long'],
        )
        pair.long = add_prefix(url=pair.long)
        db.session.add(pair)

        try:
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            if attempt < attempts:
                continue

            raise

        break

    return flask.jsonify(short=short)


@app.route('/get/<short>')
def get(short):
    pair = Pair.query.filter_by(short=short).first()

    return flask.jsonify(long=pair.long)


@app.route('/<short>')
def redirect(short):
    pair = Pair.query.filter_by(short=short).first()

    return flask.redirect(pair.long)
