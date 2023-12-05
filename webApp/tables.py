from . import db
from flask_login import UserMixin


class GTAApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    f_name = db.Column(db.String(100))
    l_name = db.Column(db.String(100))
    std_id = db.Column(db.Integer)
    app_email = db.Column(db.String(200))
    level = db.Column(db.String(3))
    grad_semester = db.Column(db.String(100))
    umkc_gpa = db.Column(db.String(4))
    umkc_hours = db.Column(db.Integer)
    undergrad = db.Column(db.String(20))
    major = db.Column(db.String(4))
    apply_for = db.Column(db.String(20))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean)
    user_app = db.relationship('GTAApplication', uselist=False, backref='user')
    submission = db.relationship('Submissions', backref='user')


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(5))
    instructor = db.Column(db.String(100))
    position = db.Column(db.String(10))
    gta_cert_req = db.Column(db.Boolean)
    class_submission = db.relationship('Submissions', backref='course')


class Submissions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    status = db.Column(db.String(100))





