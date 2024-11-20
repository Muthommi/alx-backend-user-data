#!/usr/bin/env python3
"""
Module that defines a _hash_password method that takes in
password string arguments.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """
    Hashes password using bcrypt.
    Returns: Bytes.
    """
    return hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Rgisters new users with the provided password and email.
        Returns: User: Newly created object.
        Raises: ValueError.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password.decode('utf-8'))
            return user
