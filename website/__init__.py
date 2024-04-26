from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.sqlite"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'duvet'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .view import view
    from .auth import auth

    app.register_blueprint(view, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .datamodel import User

    create_database(app)

    return app

def create_database(app):
    with app.app_context():
        if not path.exists('website/' + DB_NAME):
            db.create_all()