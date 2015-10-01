=======================================
py.test plugin to remove stale bytecode
=======================================


This plugin removes all stale bytecode files before running tests. This makes
sure that Python modules – whose source was deleted – are not accidentally visible
to the test runner anymore due to a left-over bytecode file (``*.pyc``,
``*.pyo``).

This plugin was inspired by a feature of `zope.testrunner`_.

.. _`zope.testrunner`: https://pypi.python.org/pypi/zope.testrunner
