from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name']  # Add more fields if needed
        fields = ['industry']  # Add more fields if needed
        fields = ['id']  # Add more fields if needed
