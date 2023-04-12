from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from django_hotwired.contrib.models import PublishedArchivedModel


def podcast_directory_path(instance, filename):
    return "podcasts/{0}".format(filename)


class Podcast(PublishedArchivedModel, TimeStampedModel):
    title = models.CharField(max_length=512)
    keywords = models.TextField(max_length=512, blank=True, null=True)

    audio = models.FileField(upload_to=podcast_directory_path, blank=True, null=True)
    text = models.TextField(_("Text of Podcast"), blank=True, null=True)
