#!/usr/bin/env python3
'''  ''' 
import bcrypt


def _hash_password(password: str) -> bytes:
    ''' Gets password than hases it using bcrypt '''
    pwd = password.encode('utf-8'), bcrypt.gensalt()
    return hash(pwd)
