# Copyright (c) 2012 Adi Roiban.
# See LICENSE for details.
"""
Package definition for chevah.ftpslib.
"""

from distutils import log
from setuptools import Command, find_packages, setup
import os
import shutil


class CacheCommand(Command):
    """
    Copy the sdist files to local pypi cache.
    """

    description = "copy distributable to Chevah cache folder"
    user_options = []

    def initialize_options(self):
        self.cwd = None
        self.destination_base = '~/chevah/brink/cache/pypi/'

    def finalize_options(self):
        self.cwd = os.getcwd()

    def run(self):
        assert os.getcwd() == self.cwd, (
            'Must be in package root: %s' % self.cwd)
        self.run_command('sdist')
        sdist_command = self.distribution.get_command_obj('sdist')
        for archive in sdist_command.archive_files:
            source = os.path.join(archive)
            destination = os.path.expanduser(
                self.destination_base + os.path.basename(archive))
            shutil.copyfile(source, destination)
        log.info(
            "Distributables files copied to %s " % (self.destination_base))


distribution = setup(
    name='chevah-ftplib',
    version='2.7.3-chevah2',
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
        'cache': CacheCommand,
        },
    )
