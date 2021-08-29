import os

from flask import Flask
from instance.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        from api.web_server import ronin_blueprint
        app.register_blueprint(ronin_blueprint)
        db.create_all()

    return app
