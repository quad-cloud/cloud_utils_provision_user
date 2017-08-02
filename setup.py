# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='cloud_utils',
    version='0.0.1',
    description='cloud_utils_provision_user,
    long_description=readme,
    author='Quadyster Cloud Devs',
    author_email='sgaddam@quadyster.com',
    url='https://github.com/Sanjanagaddam/Provision-User-at-AWS',
    packages=find_packages(exclude=('tests', 'docs'))
)
