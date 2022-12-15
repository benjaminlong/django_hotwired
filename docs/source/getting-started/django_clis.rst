Django CLIs
===========

    Important: All CLIs must be run with django's related python virtualenv activated


::

    $ cd path/to/django_hotwired/
    path/to/django_hotwired/ $ source venv/bin/activate
    (venv) path/to/django_hotwired/ $ python manage.py :cli_name:



Basic CLI Commands
------------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^


* To create a **normal user account**, just go to Sign Up and fill out the form.
Once you submit it, you'll see a "Verify Your E-mail Address" page.
Go to your console to see a simulated email verification message.

Copy the link into your browser.
Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::
::

    (venv) path/to/django_hotwired/ $ python manage.py createsuperuser


For convenience, you can keep your normal user logged in on Chrome and
your superuser logged in on Firefox (or similar), so that you can see
how the site behaves for both kinds of users. Using private browsing works too.
