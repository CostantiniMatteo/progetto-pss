from django import forms
from django.contrib.auth.models import User

from ..models import Collection, Item


class BeginLabellingForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
