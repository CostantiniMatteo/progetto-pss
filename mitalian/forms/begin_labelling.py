from django import forms


class BeginLabellingForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
