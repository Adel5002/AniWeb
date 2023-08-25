from django import forms
from allauth.account.forms import SignupForm, LoginForm

class CustomSignupForm(SignupForm):
    field_order = ['username', 'email', 'password1', 'password2']

    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'type': 'text', 'placeholder': 'Username'})
        self.fields['email'].widget = forms.EmailInput(attrs={'type': 'email', 'placeholder': 'Email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'type': 'password', 'placeholder': 'Confirm Password'})

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        # Дополнительные настройки полей, если необходимо
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'text', 'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Password'})

