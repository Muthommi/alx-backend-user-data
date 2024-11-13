#!/usr/bin/env python3
"""Module for basic authentication."""
from api.v1.auth.auth import Auth


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
