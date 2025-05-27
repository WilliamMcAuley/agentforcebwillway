from django import forms
from .models import Account, JobApplication

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'industry']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'] = forms.CharField(initial=self.instance.id, disabled=True)

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name']  # Adds more fields if you want to edit them.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'] = forms.CharField(initial=self.instance.id, disabled=True)