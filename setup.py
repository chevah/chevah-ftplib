# Copyright (c) 2012 Adi Roiban.
# See LICENSE for details.
"""
Package definition for chevah.ftpslib.
"""
from setuptools import Command, setup
import os

VERSION = '2.7.3.c14'


class PublishCommand(Command):
    """
    Publish the source distribution to local pypi cache and remote
    Chevah PyPi server.
    """

    description = "copy distributable to Chevah cache folder"
    user_options = []

    def initialize_options(self):
        self.cwd = None

    def finalize_options(self):
        self.cwd = os.getcwd()

    def run(self):
        assert os.getcwd() == self.cwd, (
            'Must be in package root: %s' % self.cwd)
        self.run_command('sdist')
        self.distribution.get_command_obj('sdist')
        # Upload package to Chevah PyPi server.
        upload_command = self.distribution.get_command_obj('upload')
        upload_command.repository = u'chevah'
        self.run_command('upload')


distribution = setup(
    name='chevah-ftplib',
    version=VERSION,
    maintainer="Adi Roiban",
    maintainer_email="adi.roiban@chevah.com",
    license='Python License',
    platforms='any',
    description='Backport of ftplib to Pyhon 2.5.',
    long_description=open('README').read(),
    url='http://www.chevah.com',
    namespace_packages=['chevah'],
    package_dir={'chevah.ftplib': 'ftplib'},
    packages=['chevah', 'chevah.ftplib'],
    cmdclass={
        'publish': PublishCommand,
        },
    )
