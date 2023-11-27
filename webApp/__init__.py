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
        #db.drop_all()
        #db.session.commit()
        db.create_all()
        test_email = 'cs451r@umsystem.edu'
        test_pass = '12345'
        test_user = User.query.filter_by(email=test_email).first()
        if not test_user:
            user = User(email=test_email, password=generate_password_hash(test_pass, method='pbkdf2'), is_admin=False)
            db.session.add(user)
            db.session.commit()



    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



    return app


