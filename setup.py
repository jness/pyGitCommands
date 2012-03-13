#!/usr/bin/env python
 
from setuptools import setup, find_packages
import sys, os
 
version = '0.1'
 
setup(name='pyGitCommands',
    version=version,
    description="pyGitCommands links Git commands to Python methods.",
    long_description="""pyGitCommands links Git commands to Python methods.""",
    classifiers=[],
    keywords='',
    author='Jeffrey Ness',
    author_email='jeffrey.ness@rackspace.com',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        ],
)