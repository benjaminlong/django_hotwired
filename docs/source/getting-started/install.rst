Install
=======

Depending how you are planning to deploy locally few dependencies might
be needed:

- Python3 (min: 3.8), Python3-dev
- Postgres 14
- Yarn
- Redis (Optional)


Download Code Source
--------------------

First, download source code from git and init dependencies

::

    # Download source projet from git
    $ git clone ... django_hotwired
    $ cd django_hotwired

    # Init Project Python Env
    path/to/django_hotwired $ python3 -m venv venv

    # Activage python virtual env
    path/to/django_hotwired $ source venv/bin/activate
    (venv) path/to/django_hotwired $

    # Create .env settings file form default
    (venv) path/to/django_hotwired $ cp default_env .env

    # Edit .env file
    # Feel free to update .env file regarding your configuration.


Dependencies
------------

Python
^^^^^^

Build Python dependencies

::

    $ cd path/to/django_hotwired
    # Activate Python Env
    path/to/django_hotwired $ source venv/bin/activate

    # Update pip if needed
    (venv) path/to/django_hotwired $ pip install --upgrade pip
    (venv) path/to/django_hotwired $ pip install wheel

    # Update Python Env with Local dependencies
    (venv) path/to/django_hotwired $ pip install -r requirements/local.txt

    # Update Python Env with Staging dependencies
    # Gunicorn only available on Staging.
    (venv) path/to/django_hotwired $ pip install -r requirements/staging.txt


Javascript
^^^^^^^^^^

Build Js dependencies

::

    $ cd path/to/django_hotwired/

    # Install Js dependencies
    path/to/django_hotwired $ yarn install

    # Then build using yarn and webpack
    path/to/django_hotwired $ yarn dev
    path/to/django_hotwired $ yarn build


Checking
--------

    You can use showmigrations to check if your django app has proper database configuration.

::

    $ cd path/to/backoffice/
    path/to/django_hotwired $ source venv/bin/activate
    (venv) path/to/django_hotwired $ python manage.py showmigrations
    (venv) path/to/django_hotwired $ python manage.py migrate
