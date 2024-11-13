#!/usr/bin/env python3
"""Module for basic authentication."""
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
