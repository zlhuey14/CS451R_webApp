from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_user

from . import db
from .tables import User
# Blueprints have a bunch of roots and URLs stored inside of it
# It is a way for us to separate our app out

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash('Login successful', category='success')
                #login_user(user)
                return redirect(url_for('views.dashboard'))

    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>logout</p>"
