import logging

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from django_hotwired.podcasts.forms import PodcastForm
from django_hotwired.podcasts.models import Podcast

logger = logging.getLogger("django_hotwired")


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "audio",
        "created",
        "published",
    )
    search_fields = ("title", "keywords",)
    list_filter = ("published", "status")
    form = PodcastForm
    fieldsets = (
        (
            _("Podcast"),
            {
                "classes": ("fieldset-box",),
                "fields": (
                    "title",
                    "status",
                    "keywords",
                    "audio",
                    "text",
                ),
            },
        ),
        (
            _("Dates"),
            {
                "classes": ("fieldset-box",),
                "fields": ("created", "published", "archived", "modified"),
            },
        ),
    )
    readonly_fields = ("created", "modified")
