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
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input is-primary is-rounded', 'type': 'text', 'placeholder': 'Title'}))
    column_separator = forms.ChoiceField(choices=DataScheme.SEPARATOR)
    string_character = forms.ChoiceField(choices=DataScheme.QUALIFIER)

    class Meta:
        model = DataScheme
        fields = ['title']


class ColumnCreateForm(forms.ModelForm):
    # order = forms.DecimalField(attrs={'class': 'select is-primary', 'placeholder': 'Title'})

    class Meta:
        model = Column
        fields = ['name', 'type', 'range_from', 'range_to', 'order']


DataSchemeColumnFormset = inlineformset_factory(
    DataScheme, Column, form=ColumnCreateForm,
    extra=1, can_delete=True, can_delete_extra=True
)
