#-*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

NAME = 'nkchanger'
VERSION = '0.1'
DESCRIPTION = 'Şekilli nickleri ASCII karakterine çevirir - Converts fancy nicknames to ASCII characters'
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
URL = 'https://github.com/Leo4Bey/nkchanger'
AUTHOR = 'Kemal Sayıt'
AUTHOR_EMAIL = 'kemalsayit01@gmail.com'
LICENSE = 'MIT'
KEYWORDS = 'nick, changer, nick changer, fancy nick'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    keywords=KEYWORDS,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    py_modules=["nkchanger"]
)
