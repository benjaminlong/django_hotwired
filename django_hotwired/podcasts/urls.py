from django.urls import path

from django_hotwired.podcasts.views import sync as podcasts_views

app_name = "podcasts"
urlpatterns = [
    path("podcast/", view=podcasts_views.index, name="podcast_index"),
    path("podcast/list", view=podcasts_views.list_view, name="podcast_list"),
]
