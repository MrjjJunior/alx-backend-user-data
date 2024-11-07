#!/usr/bin/env python3
'''encrypt'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''hashes password'''
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """check hash"""
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
    