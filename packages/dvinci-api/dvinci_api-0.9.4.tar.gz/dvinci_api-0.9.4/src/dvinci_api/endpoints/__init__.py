"""
This module provides the API client for interacting with the Dvinci API endpoints
related to users.

Classes:
---------
- UsersAPI: Provides methods to interact with the /dvinciUsers endpoints.

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
# flake8: noqa

from .user import UsersAPI
from .user_groups import UserGroupsAPI
from .applications import ApplicationsAPI
from .configuration import ConfigurationAPI
from .hiring_requests import HiringRequestsAPI
from .job_openings import JobOpeningsAPI
from .job_publications import JobPublicationsAPI
from .job_publication_channels import JobPublicationChannelsAPI
from .job_publication_placements import JobPublicationPlacementsAPI
from .locations import LocationsAPI
from .onboardings import OnboardingsAPI
from .org_units import OrgUnitsAPI

from .user.user_endpoints import UserEndpoints
from .user_groups.user_groups_endpoints import UserGroupsEndpoints
from .applications.application_endpoints import ApplicationEndpoints
from .configuration.configuration_endpoints import ConfigurationEndpoints
from .hiring_requests.hiring_requests_endpoints import HiringRequestsEndpoints
from .job_openings.job_openings_endpoints import JobOpeningsEndpoints
from .job_publications.job_publications_endpoints import JobPublicationsEndpoints
from .job_publication_channels.job_publication_channels_endpoints import JobPublicationChannelsEndpoints
from .job_publication_placements.job_publication_placements_endpoints import JobPublicationPlacementsEndpoints
from .locations.locations_endpoints import LocationsEndpoints
from .onboardings.onboardings_endpoints import OnboardingsEndpoints
from .org_units.org_units_endpoints import OrgUnitsEndpoints

__all__ = [
    'UsersAPI', 'UserGroupsAPI', 'ApplicationsAPI', 'ConfigurationAPI',
    'HiringRequestsAPI', 'JobOpeningsAPI', 'JobPublicationsAPI',
    'JobPublicationChannelsAPI', 'JobPublicationPlacementsAPI', 'LocationsAPI',
    'OnboardingsAPI', 'OrgUnitsAPI',
    'UserEndpoints', 'UserGroupsEndpoints', 'ApplicationEndpoints',
    'ConfigurationEndpoints', 'HiringRequestsEndpoints', 'JobOpeningsEndpoints',
    'JobPublicationsEndpoints', 'JobPublicationChannelsEndpoints',
    'JobPublicationPlacementsEndpoints', 'LocationsEndpoints', 'OnboardingsEndpoints',
    'OrgUnitsEndpoints'
]
