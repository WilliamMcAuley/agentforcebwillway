from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'industry']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'] = forms.IntegerField(initial=self.instance.id, disabled=True)