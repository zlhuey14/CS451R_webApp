from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
GTA_DB = "database.db"

def create_app():
    app = Flask('webApp')
    app.config['SECRET_KEY'] = 'jkljkljkljkl'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{GTA_DB}'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    from .tables import User, GTAApplication

    with app.app_context():
        inputs = ['Y', 'N']
        val = input('FOR TESTING PURPOSES ONLY, TYPE "Y" IF YOU NEED TO RESET THE DATABASE. ELSE TYPE "N"')
        if val not in inputs:
            val = input('INVALID INPUT, TYPE "Y" IF YOU NEED TO RESET THE DATABASE. ELSE TYPE "N"')
        if val in inputs and val == 'Y':
            db.drop_all()
            db.create_all()
        elif val in inputs and val == 'N':
            db.create_all()

            test_email = 'e404f@umsystem.edu'
            test_pass = '112233'
            test_user = User.query.filter_by(email=test_email).first()
            if not test_user:
                user = User(email=test_email, password=generate_password_hash(test_pass, method='pbkdf2'))
                db.session.add(user)
                db.session.commit()


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



    return app


