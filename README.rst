=======================================
py.test plugin to remove stale bytecode
=======================================

.. image:: https://img.shields.io/pypi/v/pytest-remove-stale-bytecode.svg
    :target: https://pypi.org/project/pytest-remove-stale-bytecode/

.. image:: https://img.shields.io/pypi/pyversions/pytest-remove-stale-bytecode.svg
    :target: https://pypi.org/project/pytest-remove-stale-bytecode/

.. image:: https://travis-ci.com/gocept/pytest-remove-stale-bytecode.svg?branch=master
    :target: https://travis-ci.com/gocept/pytest-remove-stale-bytecode

.. image:: https://dev.azure.com/gocept/pytest-remove-stale-bytecode/_apis/build/status/gocept.pytest-remove-stale-bytecode?branchName=master
    :target: https://dev.azure.com/gocept/pytest-remove-stale-bytecode


Description
===========

This plugin removes stale bytecode files of the packages under test before running tests. This makes
sure that Python modules -- whose source was deleted -- are not accidentally visible
to the test runner anymore due to a left-over bytecode file (``*.pyc``,
``*.pyo``).

.. caution::

   This plug-in only looks into the packages you are testing. If there is a stale bytecode file
   in another package it does not remove it.

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
