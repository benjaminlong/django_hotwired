from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


"""Marketing Django App

It integrates mailchimp marketing list capabilities.

By providing connectors, views and urls to submit email information
into a mailchimp audience list.

Urls:
    mailchimp/
    mailchimp/success
    mailchimp/error
Connectors:
    mailchimp
"""


class MarketingConfig(AppConfig):
    """Marketing app Config."""

    name = "django_hotwired.marketing"
    verbose_name = _("Marketing")
