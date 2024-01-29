"""
Custom forms for user authentication and registration in a Django web application.
"""

from .models import CustomUserModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.forms.widgets import TextInput, PasswordInput
from django import forms


class RegisterForm(UserCreationForm):
    """
    Custom registration form for user sign-up.
    """

    username = forms.CharField(max_length=150, help_text="")
    password1 = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), help_text=(""))

    def clean_password1(self):
        validate_password(self.cleaned_data.get("password1"), self.instance)
        return self.cleaned_data.get("password1")

    class Meta:
        model = CustomUserModel
        fields = ('username', 'email', 'name_of_school', 'class_level')


class LoginForm(AuthenticationForm):
    """
    Form for user login.
    """

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())