from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    age = forms.IntegerField(min_value=18, max_value=30, required=False)


class LoginForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
