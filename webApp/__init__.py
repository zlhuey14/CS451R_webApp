from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
GTA_DB = "database.db"

def create_app():
    app = Flask('webApp')
    app.config['SECRET_KEY'] = 'jkljkljkljkl'



    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{GTA_DB}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    from .tables import User

    with app.app_context():
        db.drop_all()
        db.create_all()
        test_email = 'cs451r@umsystem.edu'
        test_pass = '12345'

        test_user = User(email=test_email, password=test_pass)
        db.session.add(test_user)
        db.session.commit()

    return app

