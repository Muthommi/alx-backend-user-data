#!/usr/bin/env python3
""" Module to handle API authentication. """
from typing import List, TypeVar
from flask import request


class Auth:
    """Class to manage authentication."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required.
        Returns False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns value of authorization header from a request.
        Returns none.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns current user
        """
        return None
