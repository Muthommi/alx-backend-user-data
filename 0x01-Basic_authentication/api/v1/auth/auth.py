#!/usr/bin/env python3
""" Module to handle API authentication. """
from typing import List, TypeVar
from flask import request


class Auth:
    """Class to manage authentication."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required.
        Returns true if path is none or not in excluded_paths.
        """
        if path is None or not excluded_paths:
            return True

        path = path.rstrip('/')
        for ex_path in excluded_paths:
            if ex_path.rstrip('/') == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns value of authorization header from a request.
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns current user
        """
        return None
