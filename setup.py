#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = 'pymarketcap',
    version = '3.3.0',
    url = 'https://github.com/mondeja/pymarketcap',
    download_url = 'https://github.com/mondeja/pymarketcap/archive/master.zip',
    author = 'Alvaro Mondejar <mondejar1994@gmail.com>',
    author_email = 'mondejar1994@gmail.com',
    license = 'BSD License',
    packages = ['pymarketcap'],
    description = 'Python3 API and web scraper for coinmarketcap.com.',
    long_description = open('README.md','r').read(),
    keywords = ['coinmarketcap', 'cryptocurrency', 'API', 'wrapper', 'scraper', 'json', 'BTC', 'Bitcoin'],
    install_requires = requirements
)
