from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash
from .tables import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login_post():
    data = request.form
    print(data)
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        print(user)
        if not user or not check_password_hash(user.password, password):
            flash('Check your login credentials and try again.', 'error')
            return redirect(url_for('auth.login'))
        else:
            # flash('Login successful.', 'success')
            login_user(user)

        return redirect(url_for('views.home'))


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))
