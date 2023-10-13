from . import db
from flask_login import UserMixin
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))

class GTAApplication(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #
    # Fields from the GTA Application will go here.
    #
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

