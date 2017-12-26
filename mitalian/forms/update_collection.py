from django import forms


class UpdateCollectionForm(forms.Form):
    zip_file = forms.FileField()
