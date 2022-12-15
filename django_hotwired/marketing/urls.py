from django.urls import path

from django_hotwired.marketing import views

"""Marketing Urls

Urls:
- /mailchimp
- /mailchimp/success
- /mailchimp/error
- /mailchimp/bounced
"""


app_name = "marketing"
urlpatterns = [
    path("mailchimp", views.mailchimp, name="mailchimp"),
    path("mailchimp/success", views.mailchimp_success, name="mailchimp_success"),
    path("mailchimp/error", views.mailchimp_error, name="mailchimp_error"),
    path("mailchimp/bounced", views.mailchimp_error, name="mailchimp_bounced"),
]
