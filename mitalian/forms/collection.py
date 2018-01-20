from django.forms import ModelForm
from django import forms

from ..models import Collection


class CollectionForm(ModelForm):
    description = forms.CharField(required=False,
        widget=forms.Textarea(
            attrs={'class':'form-control'}
        )
    )

    class Meta:
        model = Collection
        fields = ['name', 'labels', 'description']

    def is_valid(self):
        valid = super(CollectionForm, self).is_valid()

        if not valid:
            return valid

        if len(self.cleaned_data['labels']) < 2:
            self.errors['labels'] = 'You must choose at least two labels'
            return False

        return True
