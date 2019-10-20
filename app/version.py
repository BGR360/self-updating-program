"""
This module defines the __version__ and __version_info__ variables.
These hold the current version of the application.
Their values are automatically detected by the PBR package using git tags.
"""

from pbr.version import VersionInfo

INFO = VersionInfo('app').semantic_version()
__version__ = INFO.release_string()
__version_info__ = INFO.version_tuple()
