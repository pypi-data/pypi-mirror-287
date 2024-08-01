from setuptools import setup, find_packages

setup(
    name='WhatPulse-API-Py',
    version='0.3.0',
    packages=find_packages(),
    description='Easy Module to work with WhatPulse Client API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Flörian',
    author_email='iaccidentlyatekerosin@gmail.com',
    license='GNU General Public License v3.0 or later',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='WhatPulse',
    install_requires=[],
)