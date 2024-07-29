"""
File: src/dvinci_api/core/api.py

Author: Hendrik Siemens
Date: 2024-07-27
Last modified: 2024-07-27
Version: 0.0.1
License: MIT

Description:
-------------
This module provides a class for interacting with the Dvinci API. It includes methods
to perform GET, POST, PUT, and DELETE requests, handle responses, and manage errors.

Classes:
--------
- DvinciAPI: A class to interact with the Dvinci API.

Methods:
--------
- __init__: Initializes the DvinciAPI instance with a base URL and authentication.
- _make_request: Sends an HTTP request to the API.
- get: Performs a GET request to the API.
- post: Performs a POST request to the API.
- put: Performs a PUT request to the API.
- delete: Performs a DELETE request to the API.
- _handle_response: Handles the API response and raises exceptions for errors.

Functions:
----------

References:
-----------
"""

import requests
from .auth import DvinciAuth
from ..exceptions.api_exceptions import ApiConnectionError, ApiTimeoutError, ApiError
from ..exceptions.auth_exceptions import UnauthorizedAccessError


class DvinciAPI:
    """
    A class to interact with the Dvinci API.

    :param base_url: The base URL of the Dvinci API.
    :type base_url: str
    :param auth: An instance of DvinciAuth for authentication.
    :type auth: DvinciAuth
    """

    def __init__(self, base_url: str, auth: DvinciAuth):
        """
        Initializes the DvinciAPI instance with a base URL and authentication.

        :param base_url: The base URL of the Dvinci API.
        :type base_url: str
        :param auth: An instance of DvinciAuth for authentication.
        :type auth: DvinciAuth
        """
        self.base_url = base_url
        self.auth = auth

    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Sends an HTTP request to the API.

        :param method: The HTTP method to use ('GET', 'POST', 'PUT', 'DELETE', etc.).
        :type method: str
        :param endpoint: The API endpoint to request.
        :type endpoint: str
        :param kwargs: Additional arguments to pass to the request.
        :return: The HTTP response.
        :rtype: requests.Response
        :raises ValueError: If an invalid HTTP method is provided.
        :raises ApiConnectionError: If there's a connection error with the API.
        :raises ApiTimeoutError: If the API request times out.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = self.auth.get_headers()

        try:
            response = requests.request(
                method,
                url,
                headers=headers,
                timeout=5,
                **kwargs
            )
            self._handle_response(response)
            return response
        except requests.ConnectionError as exc:
            raise ApiConnectionError("Failed to connect to the API.") from exc
        except requests.Timeout as exc:
            raise ApiTimeoutError("The API request timed out.") from exc

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """
        Performs a GET request to the API.

        :param endpoint: The API endpoint to request.
        :type endpoint: str
        :param kwargs: Additional arguments to pass to the request.
        :return: The HTTP response.
        :rtype: requests.Response
        """
        return self._make_request('GET', endpoint, **kwargs)

    def post(self, endpoint: str, data: dict, **kwargs) -> requests.Response:
        """
        Performs a POST request to the API.

        :param endpoint: The API endpoint to request.
        :type endpoint: str
        :param data: The data to send in the request body.
        :type data: dict
        :param kwargs: Additional arguments to pass to the request.
        :return: The HTTP response.
        :rtype: requests.Response
        """
        return self._make_request('POST', endpoint, json=data, **kwargs)

    def put(self, endpoint: str, data: dict, **kwargs) -> requests.Response:
        """
        Performs a PUT request to the API.

        :param endpoint: The API endpoint to request.
        :type endpoint: str
        :param data: The data to send in the request body.
        :type data: dict
        :param kwargs: Additional arguments to pass to the request.
        :return: The HTTP response.
        :rtype: requests.Response
        """
        return self._make_request('PUT', endpoint, json=data, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """
        Performs a DELETE request to the API.

        :param endpoint: The API endpoint to request.
        :type endpoint: str
        :param kwargs: Additional arguments to pass to the request.
        :return: The HTTP response.
        :rtype: requests.Response
        """
        return self._make_request('DELETE', endpoint, **kwargs)

    def _handle_response(self, response: requests.Response) -> None:
        """
        Handles the API response and raises exceptions for errors.

        :param response: The HTTP response to handle.
        :type response: requests.Response
        :raises UnauthorizedAccessError: If the response indicates unauthorized access.
        :raises ApiError: If the response contains a general API error.
        :raises requests.HTTPError: If the response contains an HTTP error.
        """
        if response.status_code == 401:
            raise UnauthorizedAccessError("Unauthorized access to the API.")
        elif response.status_code == 404:
            raise ApiError("The requested resource was not found.")
        elif response.status_code >= 400:
            raise ApiError(f"API error occurred: {response.text}")
