#! /usr/bin/env python
# -*- coding: utf-8 -*-
# from numpy.distutils.core import setup, Extension
from setuptools import setup, find_packages

setup(
    name = "diskpop",
    version = '0.0.7',
    description = "A Python code to perform protoplanetary disc population synthesis",
    author = "Alice Somigliana, Giovanni Rosotti, Marco Tazzari, Leonardo Testi, Giuseppe Lodato, Claudia Toci, Rossella Anania, Benoit Tabone",
    author_email = "alice.somigliana@eso.org",
    packages = find_packages(),
    url = "https://bitbucket.org/ltesti/diskpop/",
    license = "GPL",
    long_description = open("README.rst").read(),
    package_data = {"": ["LICENSE", "AUTHORS.rst"]},
    include_package_data = True,
    install_requires = ["numpy", "pandas", "matplotlib", "scipy", "h5py"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
    ],
)
