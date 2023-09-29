from flask import Blueprint, render_template
#Blueprints have a bunch of roots and URLs stored inside of it
#It is a way for us to separate our app out

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"


