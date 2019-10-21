"""
Usage: install_second_latest_and_update.py GITHUB_REPO [EXPECTED_VERSION]

Queries the GitHub API to install the second-most-recent version,
and runs the program to ensure that it updates to the most recent
version (specified by EXPECTED_VERSION).
"""

import sys

import requests

from common import subprocess_call_and_print, print_app_version

GITHUB_REPO = sys.argv[1]
EXPECTED_VERSION = None
if len(sys.argv) > 2:
    EXPECTED_VERSION = sys.argv[2]

print('EXPECTED_VERSION = {}'.format(EXPECTED_VERSION))

# Fetch second-to-latest version string from GitHub API
api_url = 'https://api.github.com/repos/{}/releases'.format(GITHUB_REPO)
releases = requests.get(api_url).json()
previous_version = releases[1]['tag_name']

# Install previous version
print('Installing previous version: {}'.format(previous_version))
package = 'git+https://github.com/{}.git@{}'.format(GITHUB_REPO, previous_version)
subprocess_call_and_print([sys.executable, '-m', 'pip', 'install', package])

# Run and accept any update
subprocess_call_and_print(['self-updating-app', '--yes-update'])

# Run to print version and verify it
print_app_version(expected_version=EXPECTED_VERSION)

