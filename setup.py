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
    version='7.0.dev0',

    install_requires=[
        'pytest',
    ],

    extras_require={
    },

    entry_points={
        'pytest11': [
            'removestalebytecode = pytest_remove_stale_bytecode',
        ],
    },

    author='gocept <mail@gocept.com>',
    author_email='mail@gocept.com',
    license='MIT',
    url='https://github.com/gocept/pytest-remove-stale-bytecode/',

    keywords='pytest pyc bytecode artefacts',
    classifiers="""\
Development Status :: 4 - Beta
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 3
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Programming Language :: Python :: 3.12
Programming Language :: Python :: 3.13
Programming Language :: Python :: 3.14
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Testing
"""[:-1].split('\n'),
    python_requires='>= 3.10',
    description=__doc__.strip(),
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
        'README.rst',
        'CHANGES.rst',
    )),

    zip_safe=False,
    py_modules=['pytest_remove_stale_bytecode'],
)
