from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required
from models import User, bcrypt
from . import auth


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user_id = User.create_user(username, email, password)
        flash('Account created successfully!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('signup.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.get_user_by_email(email)
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            session.permanent = True  # Oturumu kalıcı hale getirin
            return redirect(url_for('main.index'))
        flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


