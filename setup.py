# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in photos/__init__.py
from photos import __version__ as version

setup(
	name='photos',
	version=version,
	description='Open Source Alternative to Google Photos',
	author='Gavin Dsouza',
	author_email='gavin18d@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
