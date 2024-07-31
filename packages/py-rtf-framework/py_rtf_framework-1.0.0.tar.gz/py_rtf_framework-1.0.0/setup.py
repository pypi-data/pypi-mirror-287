#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages

MAJOR = 1
MINOR = 0
PATCH = 0
VERSION = f"{MAJOR}.{MINOR}.{PATCH}"


def get_install_requires():
    reqs = [
        'pyyaml>=6.0.1',
    ]
    return reqs


setup(
    name="py_rtf_framework",
    version=VERSION,
    author="liupeng",
    author_email="895876294@qq.com",
    long_description_content_type="text/markdown",
    url='',
    long_description=open('README.md', encoding="utf-8").read(),
    python_requires=">=3.11",
    install_requires=get_install_requires(),
    packages=find_packages(),
    license='Apache',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    package_data={'': ['*.csv', '*.txt', '.toml']},  # 这个很重要
    include_package_data=True
)
