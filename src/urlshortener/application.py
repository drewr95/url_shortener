import os

import flask
import flask_sqlalchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = flask_sqlalchemy.SQLAlchemy(app)


class Pair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String)
    long = db.Column(db.String)


@app.route("/")
def hello():
    return "Hello World!"
