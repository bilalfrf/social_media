# auth/routes.py
import uuid
from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required
from models import User, bcrypt, mongo
from . import auth
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_verification_email(email, confirmation_code):
    sender_email = "frfvipbl@gmail.com"
    sender_password = "bjnk qvav uwmx styy"
    receiver_email = email
    subject = "E-posta Doğrulama"
    body = (f"You can verify your email address by clicking on the verification link: "
            f"http:////127.0.0.1:5000/auth/confirm-email/{confirmation_code}")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Verification email {receiver_email} Sent to address.")
    except Exception as e:
        print(f"E-posta gönderme hatası: {str(e)}")

def is_password_strong(password):
    # Şifre uzunluğu en az 8 karakter
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    # Büyük harf, küçük harf, rakam ve özel karakter kontrolü
    if not re.search(r"[A-Z]", password):
        return False, "Password must include at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must include at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must include at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must include at least one special character."
    return True, None


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the email already exists
        existing_user = User.get_user_by_email(email)
        if existing_user:
            flash('An account with this email already exists.', 'danger')
            return redirect(url_for('auth.signup'))

        # Check if the password is strong
        is_strong, message = is_password_strong(password)
        if not is_strong:
            flash(message, 'danger')
            return redirect(url_for('auth.signup'))

        # Create a confirmation code
        confirmation_code = str(uuid.uuid4())

        # Create the user but set is_confirmed to False
        user_id = User.create_user(username, email, password, confirmation_code)

        # Send verification email
        send_verification_email(email, confirmation_code)

        flash('Account created successfully! Please check your email to verify your account.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')


@auth.route('/confirm-email/<confirmation_code>', methods=['GET'])
def confirm_email(confirmation_code):
    user = mongo.db.users.find_one({'confirmation_code': confirmation_code})

    if user:
        mongo.db.users.update_one(
            {'_id': user['_id']},
            {'$set': {'is_confirmed': True, 'confirmation_code': None}}
        )
        flash('Your email address has been successfully verified! You can now log in.', 'success')
        return redirect(url_for('auth.login'))
    else:
        flash('Invalid or expired verification link.', 'danger')
        return redirect(url_for('auth.signup'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.get_user_by_email(email)

        if user:
            if not user.is_confirmed:
                flash('Your email address is not yet verified. Please check your email.', 'danger')
                return redirect(url_for('auth.login'))

            if bcrypt.check_password_hash(user.password, password):
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


