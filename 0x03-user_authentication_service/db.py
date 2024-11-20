#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base
# My imports
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
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

    def add_user(self,
                 email: str,
                 hashed_password: str
                 ) -> User:
        ''' Method adds user '''
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user
        # try:
        #    new_usr = User(email=email, hashed_password=hashed_password)
        #    self._session.add(new_usr)
        #    self._session.commit()
        # except Exception:
        #    self._session.rollback()
        #    new_user = None
        # return new_usr

    def find_user_by(self, **kwargs) -> User:
        ''' Finds user by keyword and returns first row '''
        try:
            found = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound()
        except TypeError as e:
            raise InvalidRequestError()
        return found

    def update_user(self, user_id: int, **kwargs) -> None:
        ''' Updates user by id '''
        # findinf user to update
        try:
            user_to_update = self.find_user_by(user_id)
            if user_to_update is None:
                return

        # updating user
            for key, value in kwargs.items():
                if not hasattr(user_to_update, key):
                    raise ValueError()
                setattr(user_to_update, key, value)

            self._session.commit()

        except NoResultFound:
            raise ValueError()
