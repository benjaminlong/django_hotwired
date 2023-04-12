import factory
from faker import Faker
from factory import fuzzy

from django_hotwired.podcasts.models import Podcast

faker = Faker()


class PodcastFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Podcast

    title = faker.sentence()

    status = "draft"

    text = faker.paragraph()
    keywords = fuzzy.FuzzyText()

    audio = None
    published = None
    archived = None
