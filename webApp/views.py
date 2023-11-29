from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required
from sqlalchemy import *

from . import db
from .tables import GTAApplication, Course

# Blueprints have a bunch of routes and URLs stored inside of it
# It is a way for us to separate our app out

views = Blueprint('views', __name__)

"""
@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("dash.html", user=current_user)
"""


@views.route('/adminView')
@login_required
def admin_view():
    return render_template('adminView.html')


@views.route('/viewCourses')
def view_courses():
    return render_template('viewCourses.html', courses=Course.query.all())


@views.route('/viewCourses', methods=['GET', 'POST'])
def courses_filter():
    filterChoice1 = request.form.get('gta_filter')
    filterChoice2 = request.form.get('degree_filter')
    filterChoice3 = request.form.get('pos_filter')
    deg_search = "%{}%".format(filterChoice2)
    pos_search = "%{}%".format(filterChoice3)
    courses = Course.query.all()

    if request.method == 'POST':

        if filterChoice1 == 'true':
            if filterChoice2 == 'default':
                if filterChoice3 == 'default':
                    courses = Course.query.filter_by(gta_cert_req=True)
                else:
                    courses = Course.query.filter(and_(Course.gta_cert_req==True,
                                                  Course.position.like(pos_search)))
            elif filterChoice2 != 'default':
                if filterChoice3 == 'default':
                    courses = Course.query.filter(and_(Course.gta_cert_req==True,
                                                       Course.c_name.like(deg_search)))
                else:
                    courses = Course.query.filter(and_(Course.gta_cert_req == True,
                                                  Course.c_name.like(deg_search),
                                                  Course.position.like(pos_search)))
        elif filterChoice1 == 'false':
            if filterChoice2 == 'default':
                if filterChoice3 == 'default':
                    courses = Course.query.filter_by(gta_cert_req=False)
                else:
                    courses = Course.query.filter(and_(Course.gta_cert_req==False,
                                                  Course.position.like(pos_search)))
            elif filterChoice2 != 'default':
                if filterChoice3 == 'default':
                    courses = Course.query.filter(and_(Course.gta_cert_req==False,
                                                       Course.c_name.like(deg_search)))
                else:
                    courses = Course.query.filter(and_(Course.gta_cert_req == False,
                                                  Course.c_name.like(deg_search),
                                                  Course.position.like(pos_search)))

        if filterChoice1 == 'default' and filterChoice2 == 'default' and filterChoice3 == 'default':
            courses = Course.query.all()

        """
        if filterChoice1 == 'true':
            if filterChoice2 == 'default':
                courses = Course.query.filter_by(gta_cert_req=True)
            else:
                courses = Course.query.filter(and_(Course.gta_cert_req == True, Course.c_name.like(deg_search)))
        elif filterChoice1 == 'false':
            if filterChoice2 == 'default':
                courses = Course.query.filter_by(gta_cert_req=False)
            else:
                courses = Course.query.filter(and_(Course.gta_cert_req == False, Course.c_name.like(deg_search)))
        else:
            courses = Course.query.filter(Course.c_name.like(deg_search))

        if filterChoice1 == 'default' and filterChoice2 == 'default':
            courses = Course.query.all()
        """

        return render_template('viewCourses.html', courses=courses)


@views.route('/viewApplication')
@login_required
def view_application():
    return render_template('viewApplication.html', user=current_user)


@views.route('/courses')
@login_required
def courses():
    return render_template('courses.html', courses=courses, lab_courses=lab_courses)


@views.route('/gtaApplication')
@login_required
def gta_application():
    return render_template("gtaApplication.html", user=current_user)


@views.route('/gtaApplication', methods=['GET', 'POST'])
def gta_application_post():
    data = request.form
    print(data)
    if current_user.is_authenticated:
        if request.method == 'POST':
            f_name = request.form.get('first_name')
            l_name = request.form.get('last_name')
            std_id = request.form.get('std_id')
            app_email = request.form.get('app_email')
            level = request.form.get('level')
            grad_semester = request.form.get('grad_semester')
            umkc_gpa = request.form.get('umkc_gpa')
            umkc_hours = request.form.get('umkc_hours')
            undergrad = request.form.get('undergrad_degree')
            major = request.form.get('major')
            apply_for = request.form.get('apply_for')

            user_app = GTAApplication(user_id=current_user.id, f_name=f_name,
                                      l_name=l_name, std_id=std_id,
                                      app_email=app_email, level=level,
                                      grad_semester=grad_semester, umkc_gpa=umkc_gpa,
                                      umkc_hours=umkc_hours, undergrad=undergrad,
                                      major=major, apply_for=apply_for)
            db.session.add(user_app)
            db.session.commit()

            return redirect(url_for('views.gta_application'))


@views.route('/', methods=['GET'])
def home():
    return render_template("home.html")
