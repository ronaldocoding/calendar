from datetime import datetime
from flask_login import UserMixin
from pony.orm import Database, Required, PrimaryKey, Set


db = Database()
db.bind(provider="sqlite", filename="../agenda.db", create_db=True)


class User(UserMixin, db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    email = Required(str)
    password = Required(str)
    status = Required(int)
    __is_authenticated = Required(bool, default=False)

    @property
    def is_authenticated(self):
        return self.__is_authenticated

    def set_authenticated(self, value: bool):
        self.__is_authenticated = value

    def verify_password(self, password):
        return self.password == password


db.generate_mapping(create_tables=True)
