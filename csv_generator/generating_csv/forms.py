from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import inlineformset_factory
from .models import *


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input is-primary', 'type': 'text', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input is-primary', 'type': 'password', 'placeholder': 'Password'}))


class DataSchemeCreateForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'column_separator', 'string_character']


class DataSchemeUpdateForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'column_separator', 'string_character']


class ColumnCreateForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'type', 'order', 'range_from', 'range_to']


class ColumnUpdateForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'type', 'order', 'range_from', 'range_to']

