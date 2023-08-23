from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LoginForm(forms.Form):

    username = forms.CharField(
        label = "Username",
        max_length = 80,
        required = True,
    )
    
    password = forms.CharField(
        label = "Password",
        max_length = 80,
        required = True,
    )
