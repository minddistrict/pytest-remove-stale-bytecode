# Copyright (c) 2014-2019 gocept gmbh & co. kg
# See also LICENSE.txt

# This should be only one line. If it must be multi-line, indent the second
# line onwards to keep the PKG-INFO file format intact.
"""py.test plugin to remove stale byte code files."""

from setuptools import setup
import os.path


def project_path(*names):
    return os.path.join(os.path.dirname(__file__), *names)


setup(
    name='pytest-remove-stale-bytecode',
    version='3.0.1',

    install_requires=[
        'pytest < 3.10',
        'setuptools',
    ],

    extras_require={
    },

    entry_points={
        'pytest11': [
            'removestalebytecode = plugin',
        ],
    },

    author='gocept <mail@gocept.com>',
    author_email='mail@gocept.com',
    license='MIT',
    url='https://bitbucket.org/gocept/pytest-remove-stale-bytecode/',

    keywords='',
    classifiers="""\
Development Status :: 7 - Inactive
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Testing
"""[:-1].split('\n'),
    description=__doc__.strip(),
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
        'README.rst',
        'CHANGES.rst',
    )),

    py_modules=['plugin'],
)
