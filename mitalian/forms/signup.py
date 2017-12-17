from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=70,
        error_messages={'required': 'Please enter your name'},
        strip=True
    )
    password = forms.CharField(max_length=256,
                               widget=forms.PasswordInput)
    email = forms.EmailField(max_length=70, required=False)
# TODO multi choice models
