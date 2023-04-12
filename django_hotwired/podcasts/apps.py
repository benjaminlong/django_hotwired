from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PodcastsConfig(AppConfig):
    name = "django_hotwired.podcasts"
    verbose_name = _("Podcasts")
