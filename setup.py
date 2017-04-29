#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from pip.req import parse_requirements

__version__ = "1.0.0"
__author__ = "Orcun Gumus <gumus@somed.io>"


long_description = open('README.rst').read()

install_reqs = parse_requirements("requirements.txt", session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='fastremover',
    version=__version__,
    description='A package for help remove nodes from a network',
    long_description=long_description,
    author=__author__,
    author_email='orcungumus@gmail.com',
    install_requires=reqs,
    url='https://github.com/somedanalytics/fast-remover',  # use the URL to the github repo
    download_url='https://github.com/guemues/fast-remover/archive/1.0.0.tar.gz'
)