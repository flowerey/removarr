#-*- coding:UTF-8 -*-

from setuptools import setup, find_packages
from removarr.version import __version__

setup(name='removarr',
    version=__version__,
    description='Automatically remove torrents according to your strategies.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    classifiers = [
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ], # Get classifiers from https://pypi.org/pypi?%3Aaction=list_classifiers
    keywords = 'python autoremove torrent',
    author = 'flowerey',
    author_email = 'blu3berry@disroot.org',
    url = 'https://github.com/flowerey/removarr',
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = True,
    install_requires=[
        'deluge-client>=1.4.0',
        'ply>=3.11',
        'psutil>=5.0.0',
        'PyYAML>=5.1',
        'requests>=2.20.0',
    ],
    python_requires='>=3.7',
    entry_points = {
        'console_scripts':[
            'removarr = removarr.main:main'
        ]
    }
)