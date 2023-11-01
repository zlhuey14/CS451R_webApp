from flask import Blueprint, render_template, redirect, url_for, request

# Blueprints have a bunch of routes and URLs stored inside of it
# It is a way for us to separate our app out

views = Blueprint('views', __name__)

#>>
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name


lab_courses = [
    Course(1, 'CS 101L'), Course(2, 'CS 201L'), Course(3, 'ECE 227'),
    Course(4, 'ECE 229'), Course(5, 'ECE 227'), Course(6, 'ECE 303'),
    Course(7, 'ECE 377'), Course(8, 'ECE 331'), Course(9, 'ECE 427'),
    Course(10, 'ECE 429')
]


courses = [
    Course(1, 'CS 101'), Course(2, 'CS 191'), Course(3, 'CS 201R'),
    Course(4, 'CS 291'), Course(5, 'CS 303'), Course(6, 'CS 320'),
    Course(7, 'CS 349'), Course(8, 'CS 394R'), Course(9, 'CS 404'),
    Course(10, 'CS 441'), Course(11, 'CS 449'), Course(12, 'CS 456'),
    Course(13, 'CS 457'), Course(14, 'CS 458'), Course(15, 'CS 461'),
    Course(16, 'CS 465R'), Course(17, 'CS 470'), Course(18, 'CS 5520'),
    Course(19, 'CS 5525'), Course(20, 'CS 5552A'), Course(21, 'CS 5565'),
    Course(22, 'CS 5573'), Course(23, 'CS 5590PA'), Course(24, 'CS 5592'),
    Course(25, 'CS 5596A'), Course(26, 'CS 5596B'), Course(27, 'ECE 216'),
    Course(28, 'ECE 226'), Course(29, 'ECE 228'), Course(30, 'ECE 241'),
    Course(31, 'ECE 276'), Course(32, 'ECE 302'), Course(33, 'ECE 330'),
    Course(34, 'ECE 341R'), Course(35, 'ECE 428R'), Course(36, 'ECE 458'),
    Course(37, 'ECE 466'), Course(38, 'ECE 477'), Course(39, 'ECE 486'),
    Course(40, 'ECE 5558'), Course(41, 'ECE 5560'), Course(42, 'ECE 5567'),
    Course(43, 'ECE 5577'), Course(44, 'ECE 5578'), Course(45, 'ECE 5586'),
    Course(46, 'IT 222'), Course(47, 'IT 321')
]

"""
@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("dash.html")
"""

@views.route('/courses')
def course_list():
    return render_template('courses.html', courses=courses, lab_courses=lab_courses)


@views.route('/gtaApplication', methods=['GET', 'POST'])
def gta_application():
    return render_template("gtaApplication.html")


@views.route('/gtaApplication', methods=['GET', 'POST'])
def gta_application_post():
    data = request.form

    if request.method == 'POST':
        f_name = request.form.get('first_name')
        l_name = request.form.get('last_name')
        std_id = request.form.get('student_id')
        cur_level = request.form.get('current_level')
        grad_semester = request.form.get('grad_semester')
        gpa = request.form.get('umkc_gpa')
        hours = request.form.get('umkc_hours')
        undergrad_degree = request.form.get('undergrad_degree')
        cur_major = request.form.get('current_major')
        apply_for = request.form.get('apply_for')









