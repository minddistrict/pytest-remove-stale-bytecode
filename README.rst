=======================================
Stable bytecode removing py.test plugin
=======================================


This plugin removes all stale bytecode files before running tests. This makes
sure that removed python files are no longer visible for the test runner as
their bytecode file (``*.pyc``, ``*.pyo``) is removed as well.


Note: Under Python 3 all bytecode files are removed as its nearly unpossible to
find out to which code file it belongs.

This plugin is inspired by a feature of `zope.testrunner`_.

.. _`zope.testrunner`: https://pypi.python.org/pypi/zope.testrunner
