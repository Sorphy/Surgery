from django.shortcuts import get_object_or_404, render, redirect
from . import models
from . import forms
import os
from Surgery import settings


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


def delete_patient(request, id):
    patient = get_object_or_404(models.Patient, pk=id)
    patient.delete()
    return redirect('patients')


def update_patient(request, id):
    patient = get_object_or_404(models.Patient, pk=id)
    if request.method == 'GET':
        patient_form = forms.Patient_form(initial={
            'first_name': patient.first_name,
            'last_name': patient.last_name,
            'birthday': patient.birthday,
            'height': patient.height,
            'weight': patient.weight,
        })

        context = {
            'patient_form': patient_form,
            'patient_id': patient.id
        }
        return render(request, 'Office/patient_update.html', context)
    else:
        patient_form = forms.Patient_form(request.POST)
        if patient_form.is_valid():
            patient.first_name = patient_form.cleaned_data['first_name']
            patient.last_name = patient_form.cleaned_data['last_name']
            patient.birthday = patient_form.cleaned_data['birthday']
            patient.weight = patient_form.cleaned_data['weight']
            patient.height = patient_form.cleaned_data['height']
            patient.save()
            return redirect('patient_detail', patient.id)
        else:
            context = {
                'patient_form': forms.Patient_form(request.POST),
                'patient_id': patient.id
            }
            return render(request, 'Office/patient_update.html', context)


def add_drug(request):
    if request.method == 'GET':
        context = {
            'drug_form': forms.Drug_form()
        }
        return render(request, 'Office/add_drug.html', context)
    else:
        drug_form = forms.Drug_form(request.POST, request.FILES)
        if drug_form.is_valid():
            drug_form.save()
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


def delete_drug(request, id):
    drug = get_object_or_404(models.Drug, pk=id)
    if drug.picture.name != '':
        os.remove(settings.BASE_DIR + '/Office' + drug.picture.url)
    drug.delete()
    return redirect('drugs')


def update_drug(request, id):
    drug = get_object_or_404(models.Drug, pk=id)
    if request.method == 'GET':
        drug_form = forms.Drug_form(initial={
            'name': drug.name,
            'gram': drug.gram,
            'number_of_pills': drug.number_of_pills,
            'description': drug.description,
            'picture': ''
        })

        context = {
            'drug_form': drug_form,
            'drug_id': drug.id
        }
        return render(request, 'Office/update_drug.html', context)
    else:
        drug_form = forms.Drug_form(request.POST, request.FILES)
        if drug_form.is_valid():
            if drug_form.cleaned_data['picture'] is not None:
                drug.picture = drug_form.cleaned_data['picture']
            drug.name = drug_form.cleaned_data['name']
            drug.number_of_pills = drug_form.cleaned_data['number_of_pills']
            drug.gram = drug_form.cleaned_data['gram']
            drug.description = drug_form.cleaned_data['description']
            drug.save()
            return redirect('drug_detail', drug.id)
        else:
            context = {
                'drug_form': forms.Drug_form(request.POST),
                'drug_id': drug.id
            }
            return render(request, 'Office/update_drug.html', context)
