Django Hotwired
===============

Simple Django Project.


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT
:Test: PyTest
:Linter: Flake8


About
-----

All recent changes are logged in inside the [CHANGELOG](CHANGELOG.md) file.

- **Dependabot**: [Report]()
- TODO: Add access to flake8, unit-test and coverage reports


Documentation
-------------

The project's documentation is generated using Sphinx.
You can build the project documentation using following clis

::

  (venv) path/to/root $ cd docs
  (venv) path/to/root/docs $ make html
  (venv) path/to/root/docs $ open _build/html/index.html


Testing
-------

Type checks
^^^^^^^^^^^

Running type checks with flake8:

::

  $ flake8


Running Tests
~~~~~~~~~~~~~

To run the tests, check your test coverage, and generate an HTML coverage report

::

  $ pytest
  # Running Test Coverage
  $ coverage run -m pytest
  $ coverage html
  $ open htmlcov/index.html
