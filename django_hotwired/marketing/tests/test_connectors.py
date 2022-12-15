from django_hotwired.marketing import connectors


def test_mailchimp_client():
    mailchimp = connectors.get_mailchimp_client()
    assert mailchimp
    assert mailchimp == connectors.mailchimp


def test_mailchimp_ping():
    response = connectors.mailchimp_ping()
    assert response == {"health_status": "Everything's Chimpy!"}


# blong: We should use a Test Audience List to test new subscribers,
# and existing subscription.
def test_mailchimp_email_detail():
    _status = connectors.mailchimp_email_detail(
        "jiben2.swork@gmail.com", connectors.mailchimp_list_id
    )

    assert _status == "pending"
