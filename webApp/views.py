from flask import Blueprint, render_template
#Blueprints have a bunch of routes and URLs stored inside of it
#It is a way for us to separate our app out

views = Blueprint('views', __name__)

@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("dash.html")

@views.route('/courses')
def courses():
    return render_template("courses.html")



