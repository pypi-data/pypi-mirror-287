from setuptools import find_packages, setup
from codecs import open
from os import path

from tj_tpauth import __version__, __author__

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

SCRIPTS = [

]

PACKAGES = [
    'tj_tpauth'
]

REQUIRED_PACKAGES = [
    'aiohttp==3.9.5',
    'aiosignal==1.3.1',
    'async-timeout==4.0.3',
    'attrs==23.2.0',
    'certifi==2024.7.4',
    'charset-normalizer==3.3.2',
    'frozenlist==1.4.1',
    'idna==3.7',
    'multidict==6.0.5',
    'requests==2.32.3',
    'urllib3==2.2.2',
    'yarl==1.9.4',
]

setup(
    name='tj_tpauth',
    packages=find_packages(include=PACKAGES),
    version=__version__,
    description='The Python library helps authenticate accounts from TP Servers.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    url="https://github.com/duynguyen02/TJ-TPAuth",
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ]
)
