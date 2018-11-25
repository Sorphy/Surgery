from django import forms
from .models import Patient, Drug, Prescription
from django.forms import Textarea


class Patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = []

class Drug_form(forms.ModelForm):
    class Meta:
        model = Drug
        exclude = []

        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 50}),
        }
