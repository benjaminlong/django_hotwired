import pytest

from django.urls import reverse, resolve
from urllib.parse import urlparse

from django_hotwired.marketing import views


@pytest.mark.django_db
def test_mailchimp_views(client, anonymous_user):
    """Testing with client fixture.

    This should be the way of testing views. Using the client make sure
    run the "url" request through all the django pipeline (url-resolver,
    middlewares, views... back and force)
    """
    response = client.get(path=reverse("marketing:mailchimp"))
    assert response
    assert response.status_code == 302

    _url = urlparse(response.url)
    resolver_match = resolve(path=_url.path)

    assert resolver_match
    assert resolver_match.url_name == "user-login"


def test_mailchimp_views_unauthorized(request_factory, anonymous_user):
    # Testing mailchimp/
    request = request_factory.get(reverse("marketing:mailchimp"))
    request.user = anonymous_user
    result = views.mailchimp(request)
    assert result.status_code == 302
    assert result.url.startswith("/login")

    # Testing mailchimp/error
    request = request_factory.get(reverse("marketing:mailchimp_error"))
    request.user = anonymous_user
    result = views.mailchimp_success(request)
    assert result.status_code == 302

    # Testing mailchimp/success
    request = request_factory.get(reverse("marketing:mailchimp_success"))
    request.user = anonymous_user
    result = views.mailchimp_error(request)
    assert result.status_code == 302


@pytest.mark.django_db
def test_mailchimp_view_ok(request_factory, user):
    request = request_factory.get(reverse("marketing:mailchimp"))
    request.user = user

    result = views.mailchimp(request)
    assert result.status_code == 200


@pytest.mark.django_db
def test_mailchimp_success_view_ok(request_factory, user):
    request = request_factory.get(reverse("marketing:mailchimp_success"))
    request.user = user

    result = views.mailchimp_success(request)
    assert result.status_code == 200


@pytest.mark.django_db
def test_mailchimp_error_view_ok(request_factory, user):
    request = request_factory.get(reverse("marketing:mailchimp_error"))
    request.user = user

    result = views.mailchimp_error(request)
    assert result.status_code == 200
