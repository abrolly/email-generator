#!/usr/local/bin/python3

import subprocess
from distutils.core import setup

PATH_TO_MAIN='~/workspace/abrolly/email-generator/src/main.py'

subprocess.run(['alias', f'py-email="py {PATH_TO_MAIN}"'])

setup(
    name='email-generator',
    version='1.0',
    description='Simple python script to generate a random email and store in your clipboard.',
    author='abrolly',
    author_email='abrolly@globalization-partners.com',
    install_requires=[
        'clipboard'
    ]
)