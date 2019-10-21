"""
Usage: install_latest_from_github.py GITHUB_CLONE_REPO [EXPECTED_VERSION]

If EXPECTED_VERSION is provided, will check that the version printed by
self-updating-app --version matches.
"""

import re
import sys

GITHUB_REPO = sys.argv[1]
EXPECTED_VERSION = None
if len(sys.argv) > 2:
    EXPECTED_VERSION = sys.argv[2]

print('EXPECTED_VERSION = {}'.format(EXPECTED_VERSION))

package = 'git+{}'.format(GITHUB_REPO)
subprocess_call_and_print([sys.executable, '-m', 'pip', 'install', package])

version_output = subprocess_call_and_print(['self-updating-app', '--version'])
if EXPECTED_VERSION is not None:
    # Extract version from output
    match = re.search(r'version ([\d\.]+)', version_output)
    if match:
        version_string = match.group(1)
        assert(version_string == EXPECTED_VERSION)
        print('Version matches expected!')

subprocess_call_and_print(['self-updating-app'])

