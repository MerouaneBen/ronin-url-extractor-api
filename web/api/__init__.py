import os

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config

engine = create_engine("mariadb+mariadbconnector://" + Config.MYSQL_USER + ":" + Config.MYSQL_PASSWORD + "@" +
                       Config.MYSQL_HOST + ":" + Config.MYSQL_PORT + "/" + Config.MYSQL_DATABASE, convert_unicode=True)

db_session = scoped_session(sessionmaker(bind=engine))


def create_db_session():
    engine.dispose()
    return db_session


Base = declarative_base()
Base.query = create_db_session().query_property()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    Base.metadata.create_all(bind=engine)

    with app.app_context():
        from api.web_server import ronin_blueprint
        app.register_blueprint(ronin_blueprint)

    return app
