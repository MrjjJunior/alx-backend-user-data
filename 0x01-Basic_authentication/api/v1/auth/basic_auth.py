#!/usr/bin/env python3
''' Basic Auth
'''
from base64 import b64decode
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
