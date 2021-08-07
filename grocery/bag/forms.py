from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Groce
from django.forms.widgets import NumberInput



class GroceForm(forms.ModelForm):
    item_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Item Name",                
                "class": "form-control",
                "name" : "item_name",
            }
        ))
    item_quantity = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Item Quantity",                
                "class": "form-control",
                "name" : "item_quantity",
            }
        ))
    STATUS = (
    ('PENDING', 'PENDING'),
    ('BOUGHT', 'BOUGHT'),
    ('NOT AVAILABLE', 'NOT AVAILABLE'),
    )
    item_status = forms.ChoiceField(
        choices=STATUS,
        widget=forms.Select(
            attrs={
                "placeholder" : "Item Status",                
                "class": "form-control"
            }
        ))
    date = forms.DateField(
        widget= forms.NumberInput(
            attrs={
                "placeholder" : "YYYY-MM-DD",                
                "class": "form-control",
                "type": "date"
            }
        )
    )
    class Meta:
        model = Groce
        fields = ('item_name', 'item_quantity', 'item_status', 'date')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

