import os
import flask
import urlshortener.url

app = flask.Flask(__name__)


def createApp():
    global app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.register_blueprint(urlshortener.url.page_blueprint)
    return app