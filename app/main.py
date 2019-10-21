"""
This module defines the main() entry point as a click command.
"""

import click

from app.app import SelfUpdatingApp

# Define a command-line command using click
@click.command()
# Allow the user to install a specific version with --install-version
@click.option('--install-version',
              help='Install a specific version of the program (for testing).')
@click.option('-y', '--yes-update', is_flag=True,
              help='Automatically agree to any updates.')
@click.option('-n', '--no-update', is_flag=True,
              help='Do not check for updates.')
# Print version using --version (autodetected from setuptools)
@click.version_option()
@click.help_option('-h', '--help')
def main(install_version, yes_update, no_update):
    accept_update = None
    if yes_update:
        accept_update = True
    elif no_update:
        accept_update = False

    app = SelfUpdatingApp(accept_update=accept_update)

    if install_version:
        print('Installing version {}'.format(install_version))
        app.install_version(install_version)
        return 0

    app.run()

if __name__ == '__main__':
    main()
