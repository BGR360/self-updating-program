"""This script is used to invoke setuptools to package the application."""

from setuptools import setup

setup(
    setup_requires=['pbr'],
    pbr=True
)
