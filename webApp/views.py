from flask import Blueprint, render_template

# Blueprints have a bunch of routes and URLs stored inside of it
# It is a way for us to separate our app out

views = Blueprint('views', __name__)


class Course:
    def __init__(self, id, name, instructor, description):
        self.id = id
        self.name = name
        self.instructor = instructor
        self.description = description


courses = [
    Course(1, 'Introduction to Web Development', 'John Doe', 'Learn the basics of web development.'),
    Course(2, 'Python Programming for Beginners', 'Jane Smith', 'An introductory Python programming course.')
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


@views.route('/gtaApplication')
def gta_application():
    return render_template("gtaApplication.html")
