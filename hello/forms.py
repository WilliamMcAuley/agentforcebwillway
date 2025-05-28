from django import forms
from .models import Account, JobApplication

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'industry']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show the id field if editing an existing instance
        if self.instance and self.instance.pk:
            self.fields['id'] = forms.CharField(initial=self.instance.id, disabled=True, required=False)

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name']  # Add more fields as needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['id'] = forms.CharField(initial=self.instance.id, disabled=True, required=False)