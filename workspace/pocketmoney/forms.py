from django import forms
from .models import *

class transactions_form(forms.ModelForm):
    class Meta:
        model = transactions
        fields = ['amount','label','category']

class wallets_form(forms.ModelForm):
    class Meta:
        model = wallets
        fields = ["name"]