import hashlib
import logging

import mailchimp_marketing
from mailchimp_marketing.api_client import ApiClientError

from django.conf import settings

logger = logging.getLogger("django_hotwired")

# -----------------------------------------------------------------------------
# Mailchimp - Init Mailchimp Client from `mailchimp_marketing` package
# Importing Mailchimp settings from django settings.
mailchimp = mailchimp_marketing.Client(
    {
        "api_key": settings.MAILCHIMP_API_KEY,
        "server": settings.MAILCHIMP_SERVER_PREFIX,
        "timeout": 10,
    }
)
# Default Mailchimp audience_id we should use
mailchimp_list_id = settings.MAILCHIMP_LIST_ID


def get_mailchimp_client():
    """It returns the shared mailchimp client object.
    :returns: shared mailchimp_client
    """

    return mailchimp


def mailchimp_ping():
    """It sends a get request to mailchimp /ping API Using mailchimp shared
    client.

    :return: {"health_status": "Everything's Chimpy!"}
    :rtype: mailchimp_response
    """

    return mailchimp.ping.get()


def mailchimp_email_detail(email, list_id=mailchimp_list_id):
    """It sends a get request to mailchimp list_member to fetch email info
    Mailchimp API: Get /lists/{list_id}/members/{subscriber_hash}

    :param email: str
    :param list_id: str (Default value = mailchimp_list_id)
    :return: One of ["unknown", "error", "subscribed", "bounced", "unsubscribed", "pending"]
    :rtype: string
    """
    if email is None:
        return None

    _email_hash = hashlib.md5(email.encode("utf-8").lower()).hexdigest()
    try:
        response = mailchimp.lists.get_list_member(list_id, _email_hash)
        _status = response.get("status", None)
    except ApiClientError as error:
        if error.status_code == 404:
            return "unknown"
        return "error"

    return _status


def mailchimp_subscribe(email, status="pending", list_id=mailchimp_list_id):
    """It sends a post request to mailchimp api on `list_id`.

    :param email:
    :param status:  (Default value = "pending")
    :param list_id:  (Default value = mailchimp_list_id)
    :return: email already exists, 500, 403..., mailchimp response
    """
    if email is None:
        return

    kwargs = {
        "email_address": email,
        "status": status,
        "merge_fields": {"FNAME": "Toto", "LNAME": "Titi"},
    }

    try:
        return mailchimp.lists.add_list_member(list_id, kwargs)
    except ApiClientError as error:
        logger.debug(f"MailChimp Exception occurred: {error.text}")
        raise error


def mailchimp_update(email, status="pending", list_id=mailchimp_list_id):
    """Method takes an email and send a put request to mailchimp api on
    `list_id`.

    It supposes the email is already in the mailchimp related list_id.

    :param email:
    :param status:  (Default value = "pending")
    :param list_id:  (Default value = mailchimp_list_id)
    :return: email don't exist, 500, 403... mailchimp response
    """
    if email is None:
        return

    _email_hash = hashlib.md5(email.encode("utf-8").lower()).hexdigest()
    kwargs = {"status": status}

    try:
        return mailchimp.lists.update_list_member(list_id, _email_hash, kwargs)
    except ApiClientError as error:
        logger.debug(f"MailChimp Exception occurred: {error.text}")
        raise error
