"""
This module defines the SelfUpdatingApp class, which hosts all the application
logic.
"""

from pbr.version import SemanticVersion

from app.config import GITHUB_REPO
from app.version import __version__, get_latest_version_string_from_github_repo

class SelfUpdatingApp():
    '''A self-updating application :O'''

    def get_remote_version(self):
        '''Return the latest version available on GitHub.'''
        return get_latest_version_string_from_github_repo(GITHUB_REPO)

    def get_local_version(self):
        '''Return the currently installed version of the app.'''
        return __version__

    def is_out_of_date(self):
        '''Return True if remote version is newer than installed version.'''
        local = SemanticVersion.from_pip_string(self.get_local_version())
        remote = SemanticVersion.from_pip_string(self.get_remote_version())
        return local < remote

    def run(self):
        print('Local version: {}'.format(self.get_local_version()))
        print('Remote version: {}'.format(self.get_remote_version()))
        print('Is out of date: {}'.format(self.is_out_of_date()))
        print('Hello world!')
