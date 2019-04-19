#!/usr/bin/env python3

import setuptools


with open('README.md') as f:
    long_description = ''.join(f.readlines())


setuptools.setup(
    name='calculator',
    version='1.0',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,

    description='Calculator',
    long_description=long_description,

    # All versions are fixed just for case. Once in while try to check for new versions.
    install_requires=[
        'psycopg2==2.7.5',
    ],

    # Do not use test_require or build_require, because then it's not installed and
    # can be used only by setup.py. We want to use it manually as well.
    # Actually it could be in file like dev-requirements.txt but it's good to have
    # all dependencies close each other.
    extras_require={
        'devel': [
            'mypy==0.620',
            'pytest==3.7.1',
        ],
    },

    zip_safe=False,
)
