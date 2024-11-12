#!/usr/bin/env python3
''' Basic Auth
'''
from base64 import b64decode
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    ''' basic auth
    '''

    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        ''' extract base64 authorization header
        '''
        if authorization_header is None:
            return
        if not isinstance(authorization_header, str):
            return
        if not authorization_header.startswith('Basic '):
            return

        value = authorization_header.split(' ')[1]
        return value

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        ''' decode base64
        '''
        if not base64_authorization_header:
            return
        if not isinstance(base64_authorization_header, str):
            return
        try:
            encoded_base64 = b64decode(base64_authorization_header)
            decoded_base64 = encoded_base64.decode('utf-8')
        except Exception:
            return
        return decoded_base64

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        ''' extract user credentials
        '''
        if not decoded_base64_authorization_header:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user, password = decoded_base64_authorization_header.split(':')
        return user, password

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str
                                     ) -> TypeVar('User'):
        ''' create user object from credentials
        '''
        if not user_email or not isinstance(user_email, str):
            return
        if not user_pwd or not isinstance(user_pwd, str):
            return
        try:
            users = User.search(attributes={"email": user_email})
        except KeyError:
            return
        except Exception:
            return

        if not users:
            return
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return
