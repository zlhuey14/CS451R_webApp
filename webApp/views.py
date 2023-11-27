from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required

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

@views.route('/viewCourses')
def view_courses():
    return render_template('viewCourses.html', courses=Course.query.all())

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
        #return redirect(url_for('views.dashboard'))
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









