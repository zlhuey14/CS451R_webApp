from flask import Blueprint, render_template, request, flash, url_for, redirect
from werkzeug.security import check_password_hash
from .tables import User
auth = Blueprint('auth', __name__)


@auth.route('/', methods=['POST'])
def login_post():
    data = request.form
    print(data)
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Check your login credentials and try again.', 'error')
            return redirect(url_for('auth.login'))
        else:
            flash('Login successful.', 'success')
        return redirect(url_for('views.dashboard'))


@auth.route('/')
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>logout</p>"
