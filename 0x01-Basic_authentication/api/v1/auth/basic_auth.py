#!/usr/bin/env python3
''' Basic Auth
'''
from api.v1.auth.auth import Auth


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
