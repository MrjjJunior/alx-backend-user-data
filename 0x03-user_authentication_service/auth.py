#!/usr/bin/env python3
''' Modules hashes passwords '''
import bcrypt
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    ''' Gets password than hases it using bcrypt '''
    pwd = password.encode('utf-8')
    return hashpw(pwd, gensalt())
