#!/usr/bin/env python3
"""Module for basic authentication."""
from typing import TypeVar, Optional
from models.user import User
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """This class inherits from auth."""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts Base64 part for basic authentication.
        Retruns: str
        """
        if (authorization_header is None or
                not isinstance(authorization_header, str)):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Method to decode base64 part of the header
        Returns: str.
        """
        if (base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Method to extract user email and password
        Returns: tuple
        """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str)):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_email, user_password = (
                decoded_base64_authorization_header.split(':', 1))
        return user_email, user_password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> Optional[TypeVar('User')]:
        """
        This method returns user instance.
        Returns: User
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users or len(users) == 0:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> Optional[TypeVar('User')]:
        """
        Method to retrieve user instance.
        Returns: User
        """
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None
        base64_auth = self.authorization_header(auth_header)
        if not base64_auth:
            return None
        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if not decoded_auth:
            return None
        user_email, user_pwd = self.extract_user_credentials(decode_auth)
        if not user_email or not user_pwd:
            return None

        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
