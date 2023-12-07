from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .tables import User

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['POST', 'GET'])
def signup_post():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password')
        password2 = request.form.get('password_check')

        current_user_check = User.query.filter_by(email=email).first()

        if current_user_check:
            flash('Email already associated with an account.', 'error')
            return redirect(url_for('auth.signup'))
        elif password1 != password2:
            flash('Passwords did not match', 'error')
            return redirect(url_for('auth.signup'))
        elif len(password1) < 5:
            flash('Password must be at least 5 characters long', 'error')
            return redirect(url_for('auth.signup'))
        else:
            user = User(email=email, password=generate_password_hash(password1, method='pbkdf2'), is_admin=False)
            db.session.add(user)
            db.session.commit()
            flash('Account creation success! You can now login with your new credentials.', 'success')
            return redirect(url_for('views.home'))

    return render_template("signup.html")


@auth.route('/signup')
def signup():
    return render_template("signup.html")


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
            flash('Login successful.', 'success')
            login_user(user)

        return redirect(url_for('views.home'))


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful.', 'success')
    return redirect(url_for('views.home'))
