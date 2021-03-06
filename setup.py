#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
import sys

# get version
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'ctwrap', '_version.py')) as version_file:
    exec(version_file.read())


def readme():
    """ load readme """
    with open('README.md') as f:
        return f.read()


# configuration
setup(
    name='ctwrap',
    version=__version__,
    description='Wrapper functions for running batch simulations',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: MIT',
        'Programming Language :: Python :: 3',
    ],
    keywords='python, wrapper, cantera',
    url='https://github.com/ischoegl/ctwrap.git',
    author='Ingmar Schoegl',
    author_email='ischoegl@lsu.edu',
    license='MIT',
    packages=find_packages(),
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
    entry_points={
        'console_scripts': ['ctwrap=ctwrap.bin.ctwrap:main'],
    },
    include_package_data=True,
    install_requires=[
        'pandas>=0.24.0',
        'openpyxl',
        'pint',
        'ruamel.yaml',
    ],
    zip_safe=False)
