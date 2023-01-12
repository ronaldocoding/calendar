from src.models import db, User
from pony.flask import db_session


@db_session
def add_user(name, email, password):
    User(name=name, email=email, password=password, status=1)


@db_session
def get_user_by_id(user_id):
    return db.User.get(id=user_id)


@db_session
def get_user_by_email(user_email):
    return db.User.get(email=user_email)
