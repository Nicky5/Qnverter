import getpass
import random

import time

import sys
import os

if sys.platform == "linux" or sys.platform == "linux2":
    from os.path import join

    from setuptools import setup, find_packages
    import pathlib

    here = pathlib.Path(__file__).parent.resolve()
    long_description = open(join(here, 'README.md')).read()

    setup(
            name='Qnverter',
            version='"1.1.0"',
            packages=[''],
            url='https://github.com/Nicky5/Qnverter',
            license='MIT',
            author='nicky',
            author_email='vandini.elia@gmail.com',
            description='Python application for quick text conversions.',
            long_description=long_description,
            py_modules=["qnverter"],
            install_reqs=[i[:-1] for i in open(join(here, 'requirements.txt'), 'r').readlines()]
    )
    os.system("sudo make install")

elif sys.platform == "darwin" or sys.platform == "win32":
    print('Sorry but installing this programm through pip is not possible.')
    time.sleep(2)
    print('yet.')