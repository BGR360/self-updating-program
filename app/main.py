"""
This module defines the main() entry point as a click command.
"""

import click

from app.app import SelfUpdatingApp

# Define a command-line command using click
@click.command()
# Print version using --version (autodetected from setuptools)
@click.version_option()
@click.help_option('-h', '--help')
def main():
    self_updating_app = SelfUpdatingApp()
    self_updating_app.run()

if __name__ == '__main__':
    main()
