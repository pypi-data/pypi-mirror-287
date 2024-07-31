"""
File: src/dvinci_api/core/auth.py

Author: Hendrik Siemens
Date: 2024-07-27
Last modified: 2024-07-27
Version: 0.0.1
License: MIT

Description:
-------------
This module provides a class for handling authentication with the Dvinci API.
It includes functionality for setting up and retrieving authentication headers.

Classes:
--------
- DvinciAuth: A class to handle authentication headers for the Dvinci API.

Methods:
--------
- __init__: Initializes the DvinciAuth instance with API user and token.
- get_headers: Returns a dictionary with authentication headers required for API requests.

Functions:
----------

References:
-----------
"""


class DvinciAuth:
    """
    A class to handle authentication headers for the Dvinci API.

    :param user: The API user.
    :type user: str
    :param token: The API token.
    :type token: str
    """

    def __init__(self, user: str, token: str):
        """
        Initializes the DvinciAuth instance with API user and token.

        :param user: The API user.
        :type user: str
        :param token: The API token.
        :type token: str
        """
        self.user = user
        self.token = token

    def get_headers(self) -> dict:
        """
        Returns authentication headers required for API requests.

        :return: A dictionary containing authentication headers.
        :rtype: dict

        :Example:

        >>> auth = DvinciAuth("myApiUser", "bjOa8wvQyZWtCYYFB3xlPeC79S7xjsCgb2ZZZ92n")
        >>> headers = auth.get_headers()
        >>> print(headers)
        {'Dvinci-API-User': 'myApiUser', 'Dvinci-API-Token': 'bjOa8wvQyZWtCYYFB3xlPeC79S7xjsCgb2ZZZ92n'}
        """
        return {
            "Dvinci-API-User": self.user,
            "Dvinci-API-Token": self.token
        }
