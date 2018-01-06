import os
import flask
import urlshortener.url
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import urlshortener.database_model
import urlshortener.url

app = flask.Flask(__name__)


def createApp():
    global app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.register_blueprint(urlshortener.url.page_blueprint)
    engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    urlshortener.database_model.db_session = sqlalchemy.orm.scoped_session(sqlalchemy.orm.sessionmaker(bind=engine))
    return app