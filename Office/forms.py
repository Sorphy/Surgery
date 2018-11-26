from django import forms
from .models import Patient, Drug, Prescription
from django.forms import Textarea


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = []


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
    '''
    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = Patient.objects.all()
        self.fields['drug'].queryset = Drug.objects.all()
    '''
'''
class PrescriptionForm(forms.Form):
    patient = forms.ModelMultipleChoiceField(queryset=Patient.objects.all())
    drugs = forms.ModelMultipleChoiceField(queryset=Drug.objects.all())
    date = forms.DateField()

'''

