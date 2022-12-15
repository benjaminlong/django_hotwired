import logging

from mailchimp_marketing.api_client import ApiClientError

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.utils.translation import gettext_lazy as _

from django_hotwired.marketing.forms import MailchimpForm
from django_hotwired.marketing.connectors import (
    mailchimp_email_detail,
    mailchimp_subscribe,
    mailchimp_update,
)

logger = logging.getLogger("newsomatic")
mailchimp_error_msg = _("Our Subscription provider is currently offline")


@login_required
def mailchimp(request, template_name="marketing/mailchimp.html"):
    """Mailchimp view.

    Methods: GET, POST - turbo-frame id "mailchimp"

    :form: MailchimpForm (name, email)

    When an email is submitted, we process has following:
    - we get mailchimp information about the email
    - If email is new, we subscribe it the mailchimp list.
    - If error from mailchimp or email is "bounced", we return error view.
    - If email is "unsubscribed" in mailchimp list, we re-subscribe it.
    - If email is already subscribed in mailchimp list, we pass...
    - Then we redirect to success view.

    :param request:
    :param template_name:  (Default value = "marketing/mailchimp.html")
    :return: render("marketing/mailchimp.html")
    """
    error = None
    form = MailchimpForm(
        request.POST or None, initial={"name": request.user.get_full_name()}
    )
    if form.is_valid() and request.POST:
        _email = form.cleaned_data.get("email")
        _status = mailchimp_email_detail(email=_email)

        try:
            if _status == "error":
                return redirect(reverse("marketing:mailchimp_error"))
            elif _status == "bounced":
                return redirect(reverse("marketing:mailchimp_bounced"))
            elif _status == "unsubscribed":
                mailchimp_update(email=_email, status="pending")
            elif _status == "unknown":
                mailchimp_subscribe(email=_email)

            error = mailchimp_error_msg
            # return redirect(reverse("marketing:mailchimp_success"))
        except ApiClientError as error:
            logger.debug(f"Mailchimp Error: {error.text}")
            error = mailchimp_error_msg

    # return redirect(reverse("marketing:mailchimp_error"))
    context = {"form": form, "error": error}
    return render(request, template_name, context)


@login_required
def mailchimp_success(request, template_name="marketing/mailchimp_success.html"):
    """Mailchimp Success view.

    Methods: GET - turbo-frame id "mailchimp"
    :param request:
    :param template_name:  (Default value = "marketing/mailchimp_success.html")
    :return: render("marketing/mailchimp_success.html")
    """
    return render(request, template_name)


@login_required
def mailchimp_error(request, template_name="marketing/mailchimp_error.html"):
    """Mailchimp Error view.

    Methods: GET - turbo-frame id "mailchimp"
    INFO: mailchimp_bounced url is using `mailchimp_error` view.

    :param request:
    :param template_name:  (Default value = "marketing/mailchimp_error.html")
    :return: render("marketing/mailchimp_error.html")
    """
    return render(request, template_name)
