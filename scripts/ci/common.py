import re
import sys
from io import StringIO
from subprocess import Popen, PIPE, STDOUT

def subprocess_call_and_print(command):
    '''Run a command, print output, and return output as string.'''
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

def print_app_version(expected_version=None):
    '''Call app with --version and optionally verify the output.'''
    version_output = subprocess_call_and_print(['self-updating-app', '--version'])
    if expected_version is not None:
        # Extract version from output
        match = re.search(r'version ([\d\.]+)', version_output)
        if match:
            version_string = match.group(1)
            if version_string != expected_version:
                print('VERSION DOES NOT MATCH!')
                print('Expected: {}'.format(expected_version))
                print('Actual: {}'.format(version_string))
                sys.exit(1)
            print('Version matches expected!')

