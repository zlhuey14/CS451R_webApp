from flask import Blueprint, render_template, redirect, url_for, request, flash, get_flashed_messages, message_flashed
from flask_login import current_user, login_required
from sqlalchemy import *

from . import db
from .tables import GTAApplication, Course, Submissions, User

# Blueprints have a bunch of routes and URLs stored inside of it
# It is a way for us to separate our app out

views = Blueprint('views', __name__)

@views.route('/adminView')
@login_required
def admin_view():
    submissions_join = db.session.query(Submissions, User, Course, GTAApplication). \
        select_from(Submissions).join(User).join(Course).join(GTAApplication).all()
    return render_template('adminView.html', submissions_join=submissions_join)

@views.route('/adminView', methods=['POST'])
@login_required
def admin_action():
    if request.method == 'POST':
        if request.form.get('approve'):
            submission_id = request.form.get('approve')
            print(submission_id)
            submission_status_update = Submissions.query.get_or_404(submission_id)
            submission_status_update.status = 'Approved'
            db.session.commit()
        elif request.form.get('deny'):
            submission_id = request.form.get('deny')
            print(submission_id)
            submission_status_update = Submissions.query.get_or_404(submission_id)
            submission_status_update.status = 'Denied'
            db.session.commit()

    return render_template('adminView.html',
                           submissions_join=db.session.query(Submissions, User, Course, GTAApplication). \
                           select_from(Submissions).join(User).join(Course).join(GTAApplication).all())

@views.route('/editCourses', methods=['POST'])
def edit_courses_filter():
    courses = Course.query.all()

    if request.method == 'POST':

        if request.form.get('remove_btn'):
            course_id = request.form.get('remove_btn')
            print(course_id)
            Course.query.filter(Course.id == course_id).delete()
            db.session.commit()
            flash('Course removed.', 'success')
            return redirect(url_for('views.edit_courses'))

        elif request.form.get('button') == 'add_course':
            new_c_name = request.form.get('c_name')
            new_instructor = request.form.get('instructor')
            new_pos = request.form.get('position')
            new_gta_cert_req = request.form.get('gta_cert_req')

            # PRINTING VALUES OF HTML ENTERED FIELDS FOR TESTING
            print(new_c_name)
            print(new_instructor)
            print(new_pos)
            print(new_gta_cert_req)
            # END TEST PRINTING VALUES

            if new_gta_cert_req == 'True':
                newCourse = Course(c_name=new_c_name, instructor=new_instructor, position=new_pos, gta_cert_req=1)
                db.session.add(newCourse)
                db.session.commit()
                return redirect(url_for('views.edit_courses'))

            elif new_gta_cert_req == 'False':
                newCourse = Course(c_name=new_c_name, instructor=new_instructor, position=new_pos, gta_cert_req=0)
                db.session.add(newCourse)
                db.session.commit()
                return redirect(url_for('views.edit_courses'))


        elif request.form.get('button') == 'filter':
            filterChoice1 = request.form.get('gta_filter')
            filterChoice2 = request.form.get('degree_filter')
            filterChoice3 = request.form.get('pos_filter')
            print('filter 1: ', filterChoice1)
            print('filter 2: ', filterChoice2)
            print('filter 3: ', filterChoice3)
            deg_search = "%{}%".format(filterChoice2)
            pos_search = "%{}%".format(filterChoice3)

            if filterChoice1 == 'true':
                if filterChoice2 == 'default':
                    if filterChoice3 == 'default':
                        courses = Course.query.filter_by(gta_cert_req=True)
                    else:
                        courses = Course.query.filter(and_(Course.gta_cert_req == True,
                                                           Course.position.like(pos_search)))
                elif filterChoice2 != 'default':
                    if filterChoice3 == 'default':
                        courses = Course.query.filter(and_(Course.gta_cert_req == True,
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
                        courses = Course.query.filter(and_(Course.gta_cert_req == False,
                                                           Course.position.like(pos_search)))
                elif filterChoice2 != 'default':
                    if filterChoice3 == 'default':
                        courses = Course.query.filter(and_(Course.gta_cert_req == False,
                                                           Course.c_name.like(deg_search)))
                    else:
                        courses = Course.query.filter(and_(Course.gta_cert_req == False,
                                                           Course.c_name.like(deg_search),
                                                           Course.position.like(pos_search)))

            elif filterChoice1 == 'default':
                if filterChoice2 == 'default':
                    if filterChoice3 == 'default':
                        courses = Course.query.all()
                    else:
                        courses = Course.query.filter(Course.position.like(pos_search))

                elif filterChoice2 != 'defualt':
                    if filterChoice3 == 'default':
                        courses = Course.query.filter(Course.c_name.like(deg_search))
                    else:
                        courses = Course.query.filter(and_(Course.c_name.like(deg_search),
                                                           Course.position.like(pos_search)))

            if filterChoice1 == 'default' and filterChoice2 == 'default' and filterChoice3 == 'default':
                courses = Course.query.all()


    return render_template('editCourses.html', courses=courses)

@views.route('/editCourses')
@login_required
def edit_courses():
    return render_template('editCourses.html', courses=Course.query.all())


@views.route('/viewCourses')
def view_courses():
    return render_template('viewCourses.html', courses=Course.query.all())


@views.route('/viewCourses', methods=['GET', 'POST'])
def courses_filter():
    courses = Course.query.all()

    if request.method == 'POST':

        if request.form.get('apply_button'):
            # THESE 3 LINES ARE FOR TESTING PURPOSES
            data = request.form.get('apply_button')
            print('Course ID: ', data)
            print('Current User ID: ', current_user.id)
            #

            hasApp = GTAApplication.query.filter_by(user_id=current_user.id).first()
            print(hasApp)
            if hasApp:
                submission = Submissions(user_id=current_user.id, course_id=int(request.form.get('apply_button')),
                                         status='Pending..')
                db.session.add(submission)
                db.session.commit()
                flash('Successfully submitted.', 'success')
                print('submitted')
            else:
                flash('Please submit an application before applying.', 'error')
                print('No application on file')

        elif request.form.get('button') == 'filter':
            filterChoice1 = request.form.get('gta_filter')
            filterChoice2 = request.form.get('degree_filter')
            filterChoice3 = request.form.get('pos_filter')
            print('filter 1: ', filterChoice1)
            print('filter 2: ', filterChoice2)
            print('filter 3: ', filterChoice3)
            deg_search = "%{}%".format(filterChoice2)
            pos_search = "%{}%".format(filterChoice3)

            if filterChoice1 == 'true':
                if filterChoice2 == 'default':
                    if filterChoice3 == 'default':
                        courses = Course.query.filter_by(gta_cert_req=True)
                    else:
                        courses = Course.query.filter(and_(Course.gta_cert_req == True,
                                                           Course.position.like(pos_search)))
                elif filterChoice2 != 'default':
                    if filterChoice3 == 'default':
                        courses = Course.query.filter(and_(Course.gta_cert_req == True,
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
                        courses = Course.query.filter(and_(Course.gta_cert_req == False,
                                                           Course.position.like(pos_search)))
                elif filterChoice2 != 'default':
                    if filterChoice3 == 'default':
                        courses = Course.query.filter(and_(Course.gta_cert_req == False,
                                                           Course.c_name.like(deg_search)))
                    else:
                        courses = Course.query.filter(and_(Course.gta_cert_req == False,
                                                           Course.c_name.like(deg_search),
                                                           Course.position.like(pos_search)))

            elif filterChoice1 == 'default':
                if filterChoice2 == 'default':
                    if filterChoice3 == 'default':
                        courses = Course.query.all()
                    else:
                        courses = Course.query.filter(Course.position.like(pos_search))

                elif filterChoice2 != 'defualt':
                    if filterChoice3 == 'default':
                        courses = Course.query.filter(Course.c_name.like(deg_search))
                    else:
                        courses = Course.query.filter(and_(Course.c_name.like(deg_search),
                                                           Course.position.like(pos_search)))

            if filterChoice1 == 'default' and filterChoice2 == 'default' and filterChoice3 == 'default':
                courses = Course.query.all()

    return render_template('viewCourses.html', courses=courses)


@views.route('/viewSubmissions')
@login_required
def view_submissions():
    return render_template('viewSubmissions.html', user=current_user,
                           student_submissions=db.session.query(Submissions, User, Course). \
                           select_from(Submissions).join(User).filter(User.id == current_user.id).join(Course).all())


@views.route('/gtaApplication')
@login_required
def gta_application():
    has_app = GTAApplication.query.filter(GTAApplication.user_id == current_user.id).first()
    return render_template("gtaApplication.html", has_app=has_app)


@views.route('/gtaApplication', methods=['GET', 'POST'])
def gta_application_post():
    data = request.form
    print(data)
    if current_user.is_authenticated:
        if request.method == 'POST':
            if request.form.get('submit') == 'submit':
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

            elif request.form.get('submit') == 'resubmit':
                GTAApplication.query.filter(GTAApplication.user_id == current_user.id).delete()
                db.session.commit()

        return redirect(url_for('views.gta_application'))


@views.route('/', methods=['GET'])
def home():
    recent_courses = Course.query.order_by(Course.id.desc()).limit(3).all()
    return render_template("home.html", courses=recent_courses)
