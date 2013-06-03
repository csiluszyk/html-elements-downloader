#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import os
import sys

if os.getuid() == 0:  # root
    print >>sys.stderr, "ERROR: This setup.py cannot be run as root."
    print >>sys.stderr, "ERROR: If you want to proceed anyway, hunt this"
    print >>sys.stderr, "ERROR: message and edit the source at your own risk."
    sys.exit(2)

setup(
    name='htmlelementsdownloader',
    version = '0.1.dev',
    description='Script for downloading HTML element from given RSS feed.',
    author='Cezary Siłuszyk',
    author_email='cezarysiluszyk@gmail.com',
    url='https://github.com/czaarek/html-elements-downloader',
    install_requires=[
        "argparse",
        "feedparser",
        "lxml",
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
)
