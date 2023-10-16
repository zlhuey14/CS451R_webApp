from flask import Blueprint, render_template, redirect, url_for, request

# Blueprints have a bunch of routes and URLs stored inside of it
# It is a way for us to separate our app out

views = Blueprint('views', __name__)


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name


courses = [
    Course(1, 'CS 101'),
    Course(2, 'CS 191'),
    Course(3, 'CS 201R'),
    Course(4, 'CS 291'),
    Course(5, 'CS 303'),
    Course(6, 'CS 320'),
    Course(7, 'CS 349'),
    Course(8, 'CS 394R'),
    Course(9, 'CS 404'),
    Course(10, 'CS 441'),
    Course(11, 'CS 449'),
    Course(12, 'CS 456'),
    Course(13, 'CS 457'),
    Course(14, 'CS 458'),
    Course(15, 'CS 461'),
    Course(16, 'CS 465R'),
    Course(17, 'CS 470'),
    Course(18, 'CS 5520'),
    Course(19, 'CS 5525'),
    Course(20, 'CS 5552A'),
    Course(21, 'CS 5565'),
    Course(22, 'CS 5573'),
    Course(23, 'CS 5590PA'),
    Course(24, 'CS 5592'),
    Course(25, 'CS 5596A'),
    Course(26, 'CS 5596B'),
    Course(27, 'ECE 216'),
    Course(28, 'ECE 226'),
    Course(29, 'ECE 228'),
    Course(30, 'ECE 241'),
    Course(31, 'ECE 276'),

]


@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("dash.html")


@views.route('/courses')
def course_list():
    return render_template('courses.html', courses=courses)


@views.route('/course/<int:course_id>')
def course(course_id):
    course_info = next((course for course in courses if course.id == course_id), None)
    if course_info:
        return render_template('course.html', course=course_info)
    else:
        return 'Course not found'


@views.route('/gtaApplication', methods=['GET', 'POST'])
def gta_application():
    return render_template("gtaApplication.html")
#COMMENT