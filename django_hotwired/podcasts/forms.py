from django import forms
from django_hotwired.podcasts.models import Podcast


class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = "__all__"
        widgets = {"keywords": forms.TextInput}
