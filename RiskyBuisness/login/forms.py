from django import forms

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
        widget=forms.PasswordInput
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
