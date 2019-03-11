=======================================
py.test plugin to remove stale bytecode
=======================================


This plugin removes all stale bytecode files before running tests. This makes
sure that Python modules -- whose source was deleted -- are not accidentally visible
to the test runner anymore due to a left-over bytecode file (``*.pyc``,
``*.pyo``).

CAUTION
=======

This plug-in no longer works since py.test 3.10. See change log for details.

Usage
=====

To use this plugin you just have to install it, so it is accessible by the
pytest you are using:

+ If you are using `buildout`, add ``pytest-remove-stale-bytecode`` to the
  buildout section of your pytest runner.

+ If you are using `pip` add it to your test requirements.

Per default, there is no output generated, but if pytest is invoked in verbose
mode (``-v``), information about the deleted files is printed.

This plugin was inspired by a feature of `zope.testrunner`_.

.. _`zope.testrunner`: https://pypi.python.org/pypi/zope.testrunner
