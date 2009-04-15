#! /usr/bin/env python

from distutils.core import setup

setup(name='Twitty Twister',
    version='1.0',
    description='Twitter client for Twisted Python',
    author='Dustin Sallings',
    author_email='dustin@spy.net',
    url='http://github.com/dustin/twitty-twister/',
    packages=['twitty'],
    package_dir={'twitty': 'lib/twitty'},
    classifiers=[
        "Framework :: Twisted",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP"
    ]
)
