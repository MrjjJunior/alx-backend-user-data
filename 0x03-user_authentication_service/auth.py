#!/usr/bin/env python3
''' Modules hashes passwords '''
import bcrypt
from bcrypt import hashpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    ''' Gets password than hases it using bcrypt '''
    pwd = password.encode('utf-8')
    return hashpw(pwd, gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _db(self):
        ''' '''
        
    def register_user(self, email: str, password: str) -> User:
        ''' Method to create a new User '''
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

            # if email in User:
            #    return f"<email> already exists."

