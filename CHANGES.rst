=======
CHANGES
=======


6.1 (unreleased)
================

- Nothing changed yet.


6.0 (2023-07-07)
================

Backwards incompatible changes
------------------------------

- Drop support for Python 3.5 and 3.6.

Features
--------

- Add support for Python 3.9, 3.10, 3.11.

- Update tests to ``pytest >= 6.2``.

Other changes
-------------

- Use Github actions as CI.



5.0.1 (2020-03-04)
==================

- Calling `pytest --help` no longer breaks when this plug-in is installed.


5.0 (2020-01-17)
================

Backwards incompatible changes
------------------------------

- Drop support for Python 2.7 and PyPy2.

Features
--------

- Add support for Python 3.8.

- Migrate to Github.

- Improve for new pytest versions.

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
