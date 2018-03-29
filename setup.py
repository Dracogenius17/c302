

from setuptools import setup
from setuptools.command.install import install as _install
import os, sys

import c302
version = c302.__version__

long_description = """
c302 is a framework for generating network models in NeuroML 2 based on C elegans connectivity data.
"""

setup(
    name = 'c302',
    version=version,
    author='Padraig Gleeson and OpenWorm contributors',
    author_email='p.gleeson@gmail.com',
    packages = ['c302'],
    install_requires=[
        'numpy',
        'xlrd',
        'xlwt',
        'pyNeuroML'
    ],
    description = 'c302',
    long_description = long_description,
    license = 'MIT',
    url='http://github.com/openworm/c302',
    download_url = 'https://github.com/openworm/c302/archive/master.zip',
    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering'
    ]
)