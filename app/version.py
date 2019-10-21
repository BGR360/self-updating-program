"""
This module defines the __version__ and __version_info__ variables.
These hold the current version of the application.
Their values are automatically detected by the PBR package using git tags.

It also defines the get_latest_version_string_from_github_repo function.
"""

import requests
from pbr.version import VersionInfo

from app.config import github_api_url

INFO = VersionInfo('self_updating_app').semantic_version()
__version__ = INFO.release_string()
__version_info__ = INFO.version_tuple()

def get_latest_version_string_from_github_repo():
    req = requests.get(github_api_url() + '/releases/latest')
    api_response = req.json()
    version_string = api_response['tag_name']
    return version_string
