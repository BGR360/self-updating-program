"""
This module defines the SelfUpdatingApp class, which hosts all the application
logic.
"""

import subprocess
import sys

from pbr.version import SemanticVersion

from app.config import github_pypi_package_url
from app.version import __version__, get_latest_version_string_from_github_repo

class SelfUpdatingApp():
    '''A self-updating application :O'''

    def __init__(self, no_update=False):
        self.no_update = no_update
        # Fetch most recent version from GitHub repository
        self.remote_version = SemanticVersion.from_pip_string(
            get_latest_version_string_from_github_repo())
        # Fetch locally installed version from PBR
        self.local_version = SemanticVersion.from_pip_string(__version__)

    def is_out_of_date(self):
        '''Return True if remote version is newer than installed version.'''
        return self.local_version < self.remote_version

    def update(self):
        '''Use pip to upgrade the current installation to the newest version.'''
        package = github_pypi_package_url()
        command = [sys.executable, '-m', 'pip', 'install', '--upgrade', package]
        subprocess.check_call(command, stdout=sys.stdout, stderr=sys.stderr)

    def install_version(self, version):
        '''Install a specific version, specified as a string.'''
        package = github_pypi_package_url(version=version)
        command = [sys.executable, '-m', 'pip', 'install', package]
        subprocess.check_call(command, stdout=sys.stdout, stderr=sys.stderr)

    def prompt_yes_or_no(self, prompt=None, default=None):
        '''
        Prompt the user for yes or no and return a bool.

        Prompt the user (e.g., '[y/n]') and return True if they answer 'yes',
        'y', or 'Y', and False if they answer 'no', 'n', or 'N'.  Will re-prompt
        until the user provides either a yes or a no.

        Parameters
        ----------
        prompt : text to display before '[y/n]'
            If None, then only '[y/n]' is displayed.
        default : default response
            If True, default is yes (i.e., '[Y/n]').
            If False, default is no (i.e., '[y/N]').
            If None, there is no default, user must provide an answer (i.e., '[y/n]').

        Thank you to user fmark on StackOverflow:
        https://stackoverflow.com/questions/3041986
        '''
        if default is None:
            post_prompt = ' [y/n]'
        elif default:
            post_prompt = ' [Y/n]'
        else:
            post_prompt = ' [y/N]'

        while True:
            sys.stdout.write('{}{}'.format(prompt, post_prompt))
            choice = str(input()).lower()
            if default is not None and choice == '':
                return default
            if choice in ['yes', 'ye', 'y']:
                return True
            if choice in ['no', 'n']:
                return False
            print('Please respond with "yes" or "no" (or "y" or "n").')

    def run(self):
        if not self.no_update:
            if self.is_out_of_date():
                print('There is a new version available (v{}).'.format(
                    self.remote_version.release_string()))
                if self.prompt_yes_or_no('Would you like to update?', default=True):
                    self.update()
        print('Hello world!')
