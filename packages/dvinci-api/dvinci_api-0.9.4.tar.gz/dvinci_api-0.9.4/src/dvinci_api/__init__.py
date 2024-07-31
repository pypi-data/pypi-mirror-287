"""
File: src/dvinci_api/__init__.py

Author: Hendrik Siemens
Date: 2024-07-27
Last modified: 2024-07-27
Version: 0.0.1
License: MIT

Description:
-------------

Classes:
--------

Methods:
--------

Functions:
----------

References:
-----------

endpoints/
├───applications
├───configuration
├───hiring_requests
├───job_openings
├───job_publications
├───job_publication_channels
├───job_publication_placements
├───locations
├───onboardings
├───org_units
├───persons
├───user
└───user_groups
"""

from .core.api import DvinciAPI
from .core.auth import DvinciAuth
from .exceptions import (
    ApiException, ApiConnectionError, ApiTimeoutError,
    ApiError, AuthException, InvalidCredentialsError,
    UnauthorizedAccessError
)
from .endpoints import (
    UsersAPI, UserGroupsAPI, ApplicationsAPI, ConfigurationAPI,
    HiringRequestsAPI, JobOpeningsAPI, JobPublicationsAPI,
    JobPublicationChannelsAPI, JobPublicationPlacementsAPI, LocationsAPI,
    OnboardingsAPI, OrgUnitsAPI
)

from .endpoints import (
    UserEndpoints, UserGroupsEndpoints,
    ApplicationEndpoints, ConfigurationEndpoints,
    HiringRequestsEndpoints, JobOpeningsEndpoints,
    JobPublicationsEndpoints, JobPublicationChannelsEndpoints,
    JobPublicationPlacementsEndpoints, LocationsEndpoints,
    OnboardingsEndpoints, OrgUnitsEndpoints
)

__all__ = [
    'DvinciAPI', 'DvinciAuth',
    'ApiException', 'ApiConnectionError',
    'ApiTimeoutError', 'ApiError',
    'AuthException', 'InvalidCredentialsError',
    'UnauthorizedAccessError', 'UsersAPI',
    'UserGroupsAPI', 'ApplicationsAPI',
    'ConfigurationAPI', 'HiringRequestsAPI',
    'JobOpeningsAPI', 'JobPublicationsAPI',
    'JobPublicationChannelsAPI', 'JobPublicationPlacementsAPI',
    'LocationsAPI', 'OnboardingsAPI',
    'OrgUnitsAPI',
    'UserEndpoints', 'UserGroupsEndpoints',
    'ApplicationEndpoints', 'ConfigurationEndpoints',
    'HiringRequestsEndpoints', 'JobOpeningsEndpoints',
    'JobPublicationsEndpoints', 'JobPublicationChannelsEndpoints',
    'JobPublicationPlacementsEndpoints', 'LocationsEndpoints',
    'OnboardingsEndpoints', 'OrgUnitsEndpoints'
]
