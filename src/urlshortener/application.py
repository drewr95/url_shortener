import os
import flask
import urlshortener.url
import flask.sessions



def createApp():
    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.register_blueprint(urlshortener.url.page_blueprint)
    return app