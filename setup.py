#!/usr/bin/env python3
from setuptools import setup, find_packages
setup(
   name='env_manager',
   version='0.0.1',
   author='Robert Borges',
   author_email='robert.borges@gmail.com',
   description='A Manager for Python Virtual Environments.',
   packages=find_packages(),
   entry_points={
      'console_scripts': [
         'envm=envmanager.main:main',
      ],
   },
)
