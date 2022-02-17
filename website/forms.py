from django import forms

class LoginForm(forms.Form):
    loginLogin = forms.CharField(required=True)
    passwordLogin = forms.CharField(required=True)

class RegisterForm(forms.Form):
    loginRegister = forms.CharField(max_length=40, required=True)
    emailRegister = forms.CharField(max_length=80, required=True)
    passwordRegister = forms.CharField(max_length=40, required=True)
    repeatPasswordRegister = forms.CharField(max_length=40, required=True)