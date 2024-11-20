#!/usr/bin/env python3
"""
Module that defines a _hash_password method that takes in
password string arguments.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes password using bcrypt.
    Returns: Bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
