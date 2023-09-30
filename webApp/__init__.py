from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
GTA_DB = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jkljkljkljkl'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{GTA_DB}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    return app
