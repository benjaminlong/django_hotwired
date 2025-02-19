from django.shortcuts import render

from django_hotwired.podcasts.models import Podcast
from django_hotwired.contrib.paginators import pager


def index(request):
    """Index view
    :param request: HttpRequest
    :return: HttpResponse
    """
    queryset = Podcast.objects.all()
    podcasts = pager(queryset, request.GET.get("page"), items_per_page=20)

    context = {"podcasts": podcasts}
    return render(request, "podcasts/sync/index.html", context)


def list_view(request):
    """turbo view"""
    queryset = Podcast.objects.all()
    podcasts = pager(queryset, request.GET.get("page"), items_per_page=20)

    context = {"podcasts": podcasts}
    return render(request, "podcasts/sync/turbo/list.html", context)


def detail_view(request, pk):
    pass


def update_view(request, pk):
    pass


def create_view(request):
    pass
