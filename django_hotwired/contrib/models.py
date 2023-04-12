from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class PublishedArchivedModel(models.Model):
    ARCHIVED, DRAFT, PUBLISHED = "archived", "draft", "published"
    STATUS_CHOICES = (
        (ARCHIVED, _("Archived")),
        (DRAFT, _("Draft")),
        (PUBLISHED, _("Published")),
    )
    status = models.CharField(choices=STATUS_CHOICES, default=DRAFT, max_length=50)

    published = models.DateTimeField(null=True, blank=True)
    published_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        related_name="published_%(class)s",
        on_delete=models.SET_NULL,
    )

    archived = models.DateTimeField(null=True, blank=True)
    archived_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        related_name="archived_%(class)s",
        on_delete=models.SET_NULL,
    )

    class Meta:
        abstract = True

    def unpublish(self, user):
        self.status = self.DRAFT
        self.save()

    def publish(self, user):
        self.published_by = user
        self.published = timezone.now()
        self.status = self.PUBLISHED
        self.save()

    def archive(self, user):
        self.status = self.ARCHIVED
        self.archived = timezone.now()
        self.archived_by = user
        self.save()


class PositionModel(models.Model):
    position = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        abstract = True

    def get_parent_filter(self):
        raise Exception("Must be implemented")

    def get_children_queryset(self):
        return self.__class__._default_manager.filter(self.get_parent_filter())

    def has_next(self):
        if hasattr(self, "_has_next"):
            return self._has_next

        self._has_next = (
            self.get_children_queryset().filter(position__gt=self.position).exists()
        )
        return self._has_next

    def has_previous(self):
        if hasattr(self, "_has_previous"):
            return self._has_previous

        self._has_previous = (
            self.get_children_queryset().filter(position__lt=self.position).exists()
        )
        return self._has_previous

    def get_first(self):
        return self.get_children_queryset().order_by("position").first()

    def get_last(self):
        return self.get_children_queryset().order_by("position").last()

    def get_next(self):
        return (
            self.get_children_queryset()
            .filter(position__gt=self.position)
            .order_by("position")
            .first()
        )

    def get_previous(self):
        return (
            self.get_children_queryset()
            .filter(position__lt=self.position)
            .order_by("position")
            .last()
        )
