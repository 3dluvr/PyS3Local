#!/usr/bin/env python

PROJECT = 'PyS3Local'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Fork of mock-s3, a Python clone of fake-s3, A lightweight server clone of Amazon S3.',
    long_description=long_description,

    author='3dluvr',
    author_email='3dluvr@users.noreply.github.com',

    url='https://github.com/3dluvr/PyS3Local',
    download_url='https://github.com/3dluvr/PyS3Local/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: MIT',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=[],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'PyS3Local = PyS3Local.main:main'
            ],
        },

    zip_safe=False,
)
