from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms as django_forms

from allauth.account.forms import SignupForm, LoginForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = django_forms.TextInput(
            attrs={"id": "name", "placeholder": "Your Name"}
        )
        self.fields['email'].widget = django_forms.EmailInput(
            attrs={"id": "email", "placeholder": "Your Email"}
        )
        self.fields['password1'].widget = django_forms.PasswordInput(
            attrs={"id": "pass", "placeholder": "Password"}
        )
        self.fields['password2'].widget = django_forms.PasswordInput(
            attrs={"id": "re_pass", "placeholder": "Repeat your password"}
        )


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget = django_forms.TextInput(attrs={'id': "your_name", 'placeholder': "Your Email"})
        self.fields['password'].widget = django_forms.PasswordInput(
            attrs={'id': "your_pass", 'placeholder': "Password"})
        self.fields['remember'].widget = django_forms.CheckboxInput(
            attrs={"id": "remember-me", "class": "agree-term"}
        )
