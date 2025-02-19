import pytest

from django_hotwired.podcasts.tests.factories import PodcastFactory


@pytest.mark.django_db
def test_podcast_is_instantiable():
    podcast = PodcastFactory.create()
    assert podcast
