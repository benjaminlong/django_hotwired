from django import forms


class MailchimpForm(forms.Form):
    """MailchimpForm.

    Simple form with `name` and `email`. Used by mailchimp views to
    gather user's information and sync it with mailchimp through i/o API
    calls.
    """

    name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"class": "input"})
    )
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={"class": "input"})
    )
