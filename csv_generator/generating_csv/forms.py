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
        fields = ['title', 'column_separator', 'string_character']


class ColumnCreateForm(forms.ModelForm):
    type = forms.ChoiceField(choices=Column.TYPE, widget=forms.Select(attrs={'class': 'input is-primary',
                                                                             'type': 'select',
                                                                             'placeholder': 'Type'}))
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input is-primary', 'type': 'text',
                                      'placeholder': 'Name'}))
    order = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'input is-primary',
                                                               'type': 'number', 'min': 1}))
    range_from = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'input is-primary', 'type': 'number'}),
                                    required=False)
    range_to = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'input is-primary', 'type': 'number'}),
                                  required=False)
    DELETE = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'input is-primary is-large',
                                                                  'type': 'checkbox'}))

    class Meta:
        model = Column
        fields = ['name', 'type', 'range_from', 'range_to', 'order', 'DELETE']


DataSchemeColumnFormset = inlineformset_factory(
    DataScheme, Column, form=ColumnCreateForm,
    extra=1, can_delete=True, can_delete_extra=True
)
