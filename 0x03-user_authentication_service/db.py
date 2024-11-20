#!/usr/bin/env python3
"""
DB module
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from typing import Any


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initializa a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds new user to database.
        Returns: user: Newly created user object.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds user by keyword arguments.
        Returns: User: First user found matching the filtering
        criteria.
        """
        if not kwargs:
            raise InvalidRequestError("No arguments provided for query")
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found with the given attributes")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query arguments")

        return user

    def update_user(self, user_id: int, **kwargs: Any) -> None:
        """
        Function to update user in the database
        Raises: ValueError in invalid attribute is passed.
        """
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if not hasattr(user, key):
                    raise ValueError(f"Invalid attribute: {key}")
                setattr(user, key, value)

            self._session.commit()

        except NoResultFound:
            raise ValueError(f"User with id {user_id} not found")
