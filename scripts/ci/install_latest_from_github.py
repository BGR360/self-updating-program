"""
Usage: install_latest_from_github.py GITHUB_CLONE_REPO [EXPECTED_VERSION]

If EXPECTED_VERSION is provided, 
"""

import re
import sys
import subprocess
from io import StringIO
from subprocess import Popen, PIPE, STDOUT

GITHUB_REPO = sys.argv[1]
EXPECTED_VERSION = None
if len(sys.argv) > 2:
    EXPECTED_VERSION = sys.argv[2]

print('EXPECTED_VERSION = {}'.format(EXPECTED_VERSION))

def subprocess_call_and_print(command):
    print()
    print(' '.join(command))
    with Popen(command, stdout=PIPE, stderr=STDOUT, 
               bufsize=1, universal_newlines=True) as p, StringIO() as output:
        for line in p.stdout:
            print(line, end='')
            output.write(line)
        stdout_contents = output.getvalue()
        p.wait()
        return_code = p.returncode
    if return_code != 0:
        print('exiting, returncode={}'.format(return_code))
        sys.exit(return_code)
    return stdout_contents


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

