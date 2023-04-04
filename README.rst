Django Hotwired
===============

Simple Django Boilerplate Project.

This project is a Django Lab project. It aims to search and
find different approach to embellished server-side rendering.

The project will explore @hotwire/stimulus and @hotwire/turbo js project.
See :ref:package.json for client dependencies.


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT
:Test: PyTest
:Linter: Flake8


About
-----

All recent changes are logged in inside the CHANGELOG.md file.

- **Dependabot**: [Report]()
- TODO: Add access to flake8, unit-test and coverage reports

Current configuration:

- Python: 3.8+
- Django: last version.
- PostgresSQL db: 14+.

Client:

- Django Template engine
- yarn + webpack for scss/js/ts
- @hotwired/stimulus, @hotwired/turbo


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
