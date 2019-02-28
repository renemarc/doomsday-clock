#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0']

setup_requirements = ['pytest-runner']

test_requirements = ['pytest']

setup(
    author="René-Marc Simard",
    author_email='renemarc@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Fetch the current Doomsday Clock from TheBulletin.org",
    entry_points={
        'console_scripts': ['doomsday_clock=doomsday_clock.cli:main']
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='doomsday_clock',
    name='doomsday_clock',
    packages=find_packages(include=['doomsday_clock']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/renemarc/doomsday_clock',
    version='0.1.0',
    zip_safe=False,
)
