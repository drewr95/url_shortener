import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Pair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String, unique=True)
    long = db.Column(db.String)
