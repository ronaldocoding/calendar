from flask import Flask
from pony.flask import Pony, db_session
from src.database import get_user_by_email, get_user_by_id
from flask_login import LoginManager, login_user

app = Flask(__name__)
app.secret_key = 'Guns... lots of guns'

Pony(app)
login_manager = LoginManager(app)
login_manager.login_view = "/"


@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)


@db_session
def authenticate_user(email, password):
    user = get_user_by_email(email)
    if user.verify_password(password):
        login_user(user)
        user.set_authenticated(False)
        return True
    else:
        return False
