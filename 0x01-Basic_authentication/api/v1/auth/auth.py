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
        return False


    def authorization_header(self, request=None) -> str:
        '''Get the Authorization header value from the request'''
        return None
    

    def current_user(self, request=None) -> TypeVar('User'):
        '''Get the current user from the request'''
        return None