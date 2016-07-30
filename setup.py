"""A setuptools based setup module for pyohio2016"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'click',
    'docopt',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyohio2016',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Examples for my PyOhio 2016 CLI talk.",
    long_description=readme + '\n\n' + history,
    author="Dave Forgac",
    author_email='tylerdave@tylerdave.com',
    url='https://github.com/tylerdave/pyohio2016',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts':[
            'pyohio-argparse=pyohio2016.cli_argparse:cli',
            'pyohio-click=pyohio2016.cli_click:cli',
            'hello-argparse=pyohio2016.hello_argparse.hello',
            'hello-click=pyohio2016.hello_click.hello',
            'hello-docopt=pyohio2016.hello_docopt.hello',
            ],
        },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    keywords='pyohio2016',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
