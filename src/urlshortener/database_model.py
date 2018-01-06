import flask_sqlalchemy
import urlshortener.application

db = flask_sqlalchemy.SQLAlchemy(urlshortener.application.app)


class Pair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String, unique=True)
    long = db.Column(db.String)