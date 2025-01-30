# app.py
from flask import Flask, session
from flask_login import LoginManager
from config import Config
from models import init_app, User
from auth import auth as auth_blueprint
from main import main as main_blueprint
from datetime import timedelta


app = Flask(__name__)
app.config.from_object(Config)

init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.get_user_by_id(user_id)

# Oturum süresini ayarlayın
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)
app.config['SESSION_COOKIE_SECURE'] = False  # HTTPS kullanıyorsanız True yapın
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=365)

@app.before_request
def make_session_permanent():
    session.permanent = True

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)


