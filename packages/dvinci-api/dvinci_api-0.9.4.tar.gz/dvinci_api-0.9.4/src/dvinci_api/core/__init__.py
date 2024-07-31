"""
File: src/dvinci_api/core/__init__.py

Author: Hendrik Siemens
Date: 2024-07-27
Last modified: 2024-07-27
Version: 0.0.1
License: MIT

Description:
-------------
This module initializes the core components of the dvinci_api package.
It provides a unified interface for accessing the core functionality of the package.

Classes:
--------

Methods:
--------

Functions:
----------

References:
-----------
"""

from .api import DvinciAPI
from .auth import DvinciAuth

__all__ = [
    'DvinciAPI',
    'DvinciAuth',
]
