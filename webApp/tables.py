from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))


class GTAApplication(db.Model, UserMixin):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(100))
    l_name = db.Column(db.String(100))
    std_id = db.Column(db.Integer)
    app_email = db.Column(db.String(200))
    degree = db.Column(db.String(3))
    grad_semester = db.Column(db.String(100))
    umkc_gpa = db.Column(db.Float)
    umkc_hours = db.Column(db.Integer)
    curr_major = db.Column(db.String(4))
    apply_for = db.Column(db.String(20))


