=======================================
py.test plugin to remove stale bytecode
=======================================


This plugin removes all stale bytecode files before running tests. This makes
sure that Python modules whose source was deleted are not accidentally visible
to the test runner anymore due to a left-over bytecode file (``*.pyc``,
``*.pyo``).

Note: With Python 3, all bytecode files are removed as it is more complex in
that case to find out to which source file a given bytecode file belongs.

This plugin, including the handling of the Python 3 case, was inspired by a
feature of `zope.testrunner`_.

.. _`zope.testrunner`: https://pypi.python.org/pypi/zope.testrunner
