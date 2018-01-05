import sqlalchemy.ext.declarative
import sqlalchemy

db_session = None
Base = sqlalchemy.ext.declarative.declarative_base()

class Pair(Base):
    __tablename__ = 'pair'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    short = sqlalchemy.Column(sqlalchemy.String, unique=True)
    long = sqlalchemy.Column(sqlalchemy.String)
