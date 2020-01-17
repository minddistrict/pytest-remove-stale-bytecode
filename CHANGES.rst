=======
CHANGES
=======


5.0 (unreleased)
================

Backwards incompatible changes
------------------------------

- Drop support for Python 2.7 and PyPy2.

Features
--------

- Migrate to Github.

Bug fixes
---------

- Fix problems when running tests jobs in parallel.
  (`#2 <https://github.com/gocept/pytest-remove-stale-bytecode/issues/2>`_)


4.0 (2019-09-13)
================

Backwards incompatible changes
------------------------------

- Drop support for Python 3.4.

Features
--------

- Make work with py.test >=3.10 again.

- Add support for Python 3.7.


3.0.1 (2019-03-21)
==================

- This plug-in only works in py.test < version 3.10.
  It is broken since the merge of
  `pytest-dev/pytest#4250 <https://github.com/pytest-dev/pytest/pull/4250>`_

- Drop support for Python 3.3.


3.0 (2017-05-12)
================

- Add support for Python 3.6, PyPy2 and PyPy3.

- Do not show output by default anymore. It can be turned on with ``-v``
  option.

- Change the license from ZPL to MIT.


2.1 (2015-10-01)
================

- Also remove bytecode files under Python 3, that end with ``-PYTEST``.


2.0 (2015-10-01)
================

- Add support for removing byte code files under Python 3.


1.0 (2014-10-29)
================

- initial release
