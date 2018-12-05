from django import forms
from .models import Patient, Drug, Prescription
from django.forms import Textarea


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = []

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['birthday'].widget.attrs.update({'placeholder': '01/01/1111'})


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        exclude = []

        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 50}),
        }


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        exclude = []

    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'placeholder': '01/01/1111'})

