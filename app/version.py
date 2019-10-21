"""
This module defines the __version__ and __version_info__ variables.
These hold the current version of the application.
Their values are automatically detected by the PBR package using git tags.

It also defines the get_latest_version_string_from_github_repo function.
"""

from pbr.version import VersionInfo
import requests
from requests.compat import urljoin

INFO = VersionInfo('app').semantic_version()
__version__ = INFO.release_string()
__version_info__ = INFO.version_tuple()

def get_latest_version_string_from_github_repo(repository):
    latest_release_url = 'https://api.github.com/repos/{}/releases/latest'.format(
        repository, 'releases', 'latest')
    req = requests.get(latest_release_url)
    api_response = req.json()
    version_string = api_response['tag_name']
    return version_string
