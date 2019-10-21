"""
Usage: install_latest_from_github.py GITHUB_CLONE_REPO [EXPECTED_VERSION]

If EXPECTED_VERSION is provided, will check that the version printed by
self-updating-app --version matches.
"""

import sys

from common import subprocess_call_and_print, print_app_version

GITHUB_REPO = sys.argv[1]
EXPECTED_VERSION = None
if len(sys.argv) > 2:
    EXPECTED_VERSION = sys.argv[2]

print('EXPECTED_VERSION = {}'.format(EXPECTED_VERSION))

# Install latest version from GitHub
package = 'git+{}'.format(GITHUB_REPO)
subprocess_call_and_print([sys.executable, '-m', 'pip', 'install', package])

# Verify app version
print_app_version(expected_version=EXPECTED_VERSION)

subprocess_call_and_print(['self-updating-app'])

