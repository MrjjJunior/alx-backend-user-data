#!/usr/bin/env python3
''' Authentication '''
from flask import request
from typing import List, TypeVar


class Auth():
    '''Authentication'''

    def require_auth(
            self,
            path: str,
            excluded_paths: List[str]
            ) -> bool:
        '''Check if the request contains a valid JWT'''
        if path and not path.endswith('/'):
            path = path + '/'
        if not path or path not in excluded_paths:
            return True
        if not excluded_paths or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        return False

    def authorization_header(self, request=None) -> str:
        '''Get the Authorization header value from the request'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Get the current user from the request'''
        return None
