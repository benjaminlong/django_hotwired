import pytest

from django_hotwired.marketing import forms


@pytest.mark.parametrize(
    "data,is_valid,expected_errors",
    [
        ({}, False, ["name", "email"]),
        ({"name": "toto"}, False, ["email"]),
        ({"email": "toto@test.fr"}, False, ["name"]),
        ({"name": "toto", "email": "toto@test.fr"}, True, []),
    ],
)
def test_mailchimp_form(data, is_valid, expected_errors):
    form = forms.MailchimpForm(data)
    assert is_valid == form.is_valid()

    if expected_errors:
        assert set(expected_errors).issubset(form.errors.keys())
        return
