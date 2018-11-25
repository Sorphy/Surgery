from django.shortcuts import get_object_or_404, render, redirect
from . import models
from . import forms
# Create your views here.


def index(request):
    return render(request, 'Office/index.html')


def patient(request):
    context = {
        'patients': models.Patient.objects.all()
    }
    return render(request, 'Office/patients.html', context)


def patient_detail(request, id):
    context = {
         'patient': get_object_or_404(models.Patient, pk=id)
    }

    return render(request, 'Office/patient_detail.html', context)


def add_patient(request):
    if request.method == 'GET':
        context = {
            'patient_form': forms.Patient_form()
        }
        return render(request, 'Office/add_patient.html', context)
    else:
        patient_form = forms.Patient_form(request.POST)
        if patient_form.is_valid():
            patient = patient_form.save(commit=False)
            patient.save()
            return redirect('patients')
        else:
            context = {
                'patient_form': forms.Patient_form(request.POST)
            }
            return render(request, 'Office/add_patient.html', context)

def add_drug(request):
    if request.method == 'GET':
        context = {
            'drug_form': forms.Drug_form()
        }
        return render(request, 'Office/add_drug.html', context)
    else:
        drug_form = forms.Drug_form(request.POST)
        if drug_form.is_valid():
            drug = drug_form.save(commit=False)
            drug.save()
            return redirect('drugs')
        else:
            context = {
                'drug_form': forms.Drug_form(request.POST)
            }
            return render(request, 'Office/add_drug.html', context)


def drugs(request):
    context = {
        'drugs': models.Drug.objects.all()
    }
    return render(request, 'Office/drugs.html', context)


def drug_detail(request, id):
    context = {
         'drug': get_object_or_404(models.Drug, pk=id)
    }

    return render(request, 'Office/drug_detail.html', context)

